"""
Model Validation Tests for Workload Forecasting and Outcome Prediction Pipeline.
"""

import json
from pathlib import Path
import numpy as np
import pytest

from src.models.workload_forecasting import WorkloadForecaster
from src.models.outcome_prediction import OutcomePredictionPipeline, LEAKAGE_FORBIDDEN_FIELDS


def test_workload_forecaster_evaluation():
    forecaster = WorkloadForecaster()
    report = forecaster.run_all()

    assert "filings_forecast" in report
    assert "pendency_forecast" in report

    filings = report["filings_forecast"]
    assert "model_evaluations" in filings
    models = filings["model_evaluations"]

    assert "naive_baseline" in models
    assert "moving_average" in models
    assert "exponential_smoothing" in models
    assert "poisson_glm" in models
    assert "arima" in models

    for name, res in models.items():
        assert "mae" in res["metrics"]
        assert "rmse" in res["metrics"]
        assert "mape_pct" in res["metrics"]
        assert res["metrics"]["mae"] >= 0

    assert "projection_2025" in filings["future_projections"]
    assert filings["future_projections"]["projection_2025"]["point_forecast"] > 20000


def test_outcome_prediction_leakage_audit():
    pipeline = OutcomePredictionPipeline()

    clean_features = ["petitioner_type", "marriage_duration_years", "legal_statute", "court_tier"]
    is_clean, leaks = pipeline.verify_feature_leakage(clean_features)
    assert is_clean is True
    assert len(leaks) == 0

    leaky_features = ["petitioner_type", "disposal_date", "final_order_date"]
    is_clean_leaky, leaks_detected = pipeline.verify_feature_leakage(leaky_features)
    assert is_clean_leaky is False
    assert "disposal_date" in leaks_detected
    assert "final_order_date" in leaks_detected


def test_outcome_prediction_pipeline_execution():
    pipeline = OutcomePredictionPipeline()
    rep = pipeline.run_pipeline()

    assert rep["leakage_audit_passed"] is True
    assert "most_frequent_baseline" in rep["candidate_model_results"]
    assert "logistic_regression_l2" in rep["candidate_model_results"]
    assert "decision_tree" in rep["candidate_model_results"]
    assert "random_forest" in rep["candidate_model_results"]

    # Verify governance restriction
    assert rep["deployment_governance_status"]["individual_probability_deployment_allowed"] is False
