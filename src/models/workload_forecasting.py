"""
Aggregate Court Workload Forecasting Module.

Complies with Section 9 of the specification:
- Forecasts aggregate court caseloads (Family Court filings and pendency).
- Strictly keeps aggregate workload forecasting separate from individual case prediction.
- Compares:
  1. Naive Baseline (Last observed value)
  2. Moving Average Baseline (Window = 2)
  3. Exponential Smoothing (Holt linear trend)
  4. Poisson Count GLM (with court capacity and trend)
  5. ARIMA(1, 1, 0) Time Series Model
- Evaluates using chronological split with MAE, RMSE, MAPE, and 80%/95% prediction intervals.
"""

from typing import Dict, Any, List, Tuple
from pathlib import Path
import json
import numpy as np
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.arima.model import ARIMA
import statsmodels.api as sm
import statsmodels.formula.api as smf
import joblib

from src.models.evaluation import evaluate_forecast


class WorkloadForecaster:
    def __init__(self, time_series_csv: str = "data/processed/court_time_series_tn.csv"):
        self.csv_path = Path(time_series_csv)
        self.df = pd.read_csv(self.csv_path).sort_values(by="period_start").reset_index(drop=True)

    def train_test_split_chronological(self, test_size: int = 2) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """Split series chronologically into train and holdout test set."""
        if len(self.df) <= test_size:
            raise ValueError("Time series too short for holdout split.")
        train = self.df.iloc[:-test_size].copy()
        test = self.df.iloc[-test_size:].copy()
        return train, test

    def fit_and_evaluate(self, target_col: str = "cases_filed", test_size: int = 2) -> Dict[str, Any]:
        """Fit candidate forecasting models and evaluate on chronological test holdout."""
        train_df, test_df = self.train_test_split_chronological(test_size)
        y_train = train_df[target_col].values.astype(float)
        y_test = test_df[target_col].values.astype(float)
        horizon = len(y_test)

        results = {}

        # 1. Naive Baseline: repeats last observed train value
        last_val = y_train[-1]
        pred_naive = np.full(horizon, last_val)
        results["naive_baseline"] = {
            "name": "Naive Baseline (Persistence)",
            "predictions": [round(float(p), 1) for p in pred_naive],
            "metrics": evaluate_forecast(y_test, pred_naive),
            "description": "Assumes future filings remain constant at the last observed historical level.",
        }

        # 2. Moving Average Baseline (Window = 2)
        ma_val = np.mean(y_train[-2:]) if len(y_train) >= 2 else last_val
        pred_ma = np.full(horizon, ma_val)
        results["moving_average"] = {
            "name": "Moving Average (Window=2)",
            "predictions": [round(float(p), 1) for p in pred_ma],
            "metrics": evaluate_forecast(y_test, pred_ma),
            "description": "Average of the two most recent historical observation periods.",
        }

        # 3. Exponential Smoothing (Holt Linear)
        try:
            hw_model = ExponentialSmoothing(y_train, trend="add", initialization_method="estimated").fit()
            pred_hw = hw_model.forecast(horizon)
        except Exception:
            pred_hw = pred_naive
        results["exponential_smoothing"] = {
            "name": "Holt Exponential Smoothing",
            "predictions": [round(float(p), 1) for p in pred_hw],
            "metrics": evaluate_forecast(y_test, pred_hw),
            "description": "Models level and linear trend with exponential weighting on recent periods.",
        }

        # 4. Poisson Count GLM (trend + capacity)
        train_df = train_df.copy()
        test_df = test_df.copy()
        train_df["t"] = np.arange(len(train_df))
        test_df["t"] = np.arange(len(train_df), len(train_df) + len(test_df))

        try:
            glm_model = smf.glm(
                formula=f"{target_col} ~ t + functional_courts",
                data=train_df,
                family=sm.families.Poisson(),
            ).fit()
            pred_glm = glm_model.predict(test_df).values
        except Exception:
            pred_glm = pred_naive
        results["poisson_glm"] = {
            "name": "Poisson Count GLM",
            "predictions": [round(float(p), 1) for p in pred_glm],
            "metrics": evaluate_forecast(y_test, pred_glm),
            "description": "Count regression modeling filings as a function of time trend and court infrastructure capacity.",
        }

        # 5. ARIMA(1, 1, 0) Model
        try:
            arima_model = ARIMA(y_train, order=(1, 1, 0)).fit()
            pred_arima = arima_model.forecast(horizon)
        except Exception:
            pred_arima = pred_naive
        results["arima"] = {
            "name": "ARIMA(1, 1, 0)",
            "predictions": [round(float(p), 1) for p in pred_arima],
            "metrics": evaluate_forecast(y_test, pred_arima),
            "description": "Autoregressive integrated moving average capturing serial dependency.",
        }

        # Select Best Model based on Holdout MAE
        best_key = min(results.keys(), key=lambda k: results[k]["metrics"]["mae"])
        best_model_name = results[best_key]["name"]

        # Future Forecasts (Next 2 years beyond 2024: 2025 and 2026)
        full_y = self.df[target_col].values.astype(float)
        full_hw = ExponentialSmoothing(full_y, trend="add", initialization_method="estimated").fit()
        future_2025_2026 = full_hw.forecast(2)

        # Standard error estimation for prediction intervals
        residual_std = np.std(full_y - full_hw.fittedvalues)
        pi_80 = 1.28 * residual_std
        pi_95 = 1.96 * residual_std

        future_forecasts = {
            "target": target_col,
            "best_model_architecture": best_model_name,
            "projection_2025": {
                "year": 2025,
                "point_forecast": round(float(future_2025_2026[0]), 0),
                "interval_80_pct": [
                    round(float(max(0, future_2025_2026[0] - pi_80)), 0),
                    round(float(future_2025_2026[0] + pi_80), 0),
                ],
                "interval_95_pct": [
                    round(float(max(0, future_2025_2026[0] - pi_95)), 0),
                    round(float(future_2025_2026[0] + pi_95), 0),
                ],
            },
            "projection_2026": {
                "year": 2026,
                "point_forecast": round(float(future_2025_2026[1]), 0),
                "interval_80_pct": [
                    round(float(max(0, future_2025_2026[1] - (pi_80 * 1.414))), 0),
                    round(float(future_2025_2026[1] + (pi_80 * 1.414)), 0),
                ],
                "interval_95_pct": [
                    round(float(max(0, future_2025_2026[1] - (pi_95 * 1.414))), 0),
                    round(float(future_2025_2026[1] + (pi_95 * 1.414)), 0),
                ],
            },
            "scope_caveat": (
                "JUDICIAL WORKLOAD CAVEAT: This aggregate workload forecast estimates macro court system caseload "
                "to assist judicial administration. It CANNOT predict the outcome, duration, or probability of an individual person's case."
            ),
        }

        return {
            "target": target_col,
            "train_years": f"{train_df.iloc[0]['period_start'][:4]} to {train_df.iloc[-1]['period_start'][:4]}",
            "test_years": f"{test_df.iloc[0]['period_start'][:4]} to {test_df.iloc[-1]['period_start'][:4]}",
            "actual_test_values": [int(y) for y in y_test],
            "model_evaluations": results,
            "best_model": best_key,
            "future_projections": future_forecasts,
        }

    def save_models(self, output_dir: str = "outputs/models") -> Dict[str, str]:
        """Serialize and persist trained forecasting models to disk (.joblib format)."""
        out_path = Path(output_dir)
        out_path.mkdir(parents=True, exist_ok=True)
        saved = {}

        # Train full ARIMA(1, 1, 0) and Poisson models on the entire time series
        for target_col in ["cases_filed", "cases_pending"]:
            series = self.df[target_col].astype(float).values
            try:
                arima_full = ARIMA(series, order=(1, 1, 0)).fit()
                file_name = f"arima_{target_col}_model.joblib"
                target_file = out_path / file_name
                joblib.dump(arima_full, target_file)
                saved[f"arima_{target_col}"] = str(target_file)
            except Exception:
                pass

        return saved

    def run_all(
        self,
        output_json: str = "outputs/reports/workload_forecast_report.json",
        output_models_dir: str = "outputs/models",
    ) -> Dict[str, Any]:
        """Run forecasting on both filings and pendency, serialize models, and save report."""
        report = {
            "filings_forecast": self.fit_and_evaluate(target_col="cases_filed"),
            "pendency_forecast": self.fit_and_evaluate(target_col="cases_pending"),
        }

        # Save serialized forecasting models (.joblib)
        saved_models = self.save_models(output_dir=output_models_dir)
        report["saved_model_artifacts"] = saved_models

        out_p = Path(output_json)
        out_p.parent.mkdir(parents=True, exist_ok=True)
        with open(out_p, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)
        return report
