"""
Script to generate standalone research figures and summary tables.

Complies with Section 14 (Results and figures) and Section 11 of the specification:
- Generates publication-ready figures in outputs/figures/
- Exports tabular datasets in outputs/tables/
"""

import sys
from pathlib import Path

# Add workspace root to sys.path
workspace_root = Path(__file__).resolve().parent.parent.parent
if str(workspace_root) not in sys.path:
    sys.path.insert(0, str(workspace_root))

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from src.cleaning.demographic_cleaner import DemographicCleaner
from src.cleaning.court_cleaner import CourtCleaner, VERIFIED_ANNUAL_FAMILY_COURT_SERIES
from src.statistics.statistical_lab import StatisticalLab
from src.models.workload_forecasting import WorkloadForecaster


def generate_all_artifacts():
    fig_dir = Path("outputs/figures")
    tab_dir = Path("outputs/tables")
    fig_dir.mkdir(parents=True, exist_ok=True)
    tab_dir.mkdir(parents=True, exist_ok=True)

    # 1. Load datasets
    df_demo = pd.read_csv("data/processed/demographic_tn_2011.csv")
    df_court_ts = pd.read_csv("data/processed/court_time_series_tn.csv")
    df_court_dist = pd.read_csv("data/processed/court_districts_pendency_tn.csv")

    plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")

    # ---------------------------------------------------------
    # Figure 1: Judicial Time Series & COVID Disruption
    # ---------------------------------------------------------
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    years = [int(p[:4]) for p in df_court_ts["period_start"]]
    ax1.plot(years, df_court_ts["cases_filed"], marker="o", color="#1d4ed8", linewidth=2.5, label="Cases Filed (Instituted)")
    ax1.plot(years, df_court_ts["cases_disposed"], marker="s", color="#15803d", linewidth=2.5, label="Cases Disposed")
    ax1.plot(years, df_court_ts["cases_pending"], marker="^", color="#b91c1c", linewidth=2.5, linestyle="--", label="Cases Pending (Year-End)")

    # Annotate COVID-19 dip in 2020
    ax1.annotate(
        "COVID-19 Disruption\n(-37.8% Filings)",
        xy=(2020, 18320),
        xytext=(2019.2, 12000),
        arrowprops=dict(facecolor="#334155", shrink=0.08, width=1.5, headwidth=6),
        fontsize=9,
        fontweight="bold",
        color="#334155",
    )

    ax1.set_title("Tamil Nadu Family Courts: Annual Caseload Dynamics (2018–2024)", fontsize=13, fontweight="bold", pad=12)
    ax1.set_xlabel("Year", fontsize=11)
    ax1.set_ylabel("Number of Cases", fontsize=11)
    ax1.legend(loc="center right", frameon=True)
    ax1.grid(True, linestyle=":", alpha=0.6)
    plt.tight_layout()
    fig1.savefig(fig_dir / "figure_1_judicial_trends_covid.png", dpi=300)
    plt.close(fig1)

    # ---------------------------------------------------------
    # Figure 2: Sex Disparity across Age Brackets (Census 2011)
    # ---------------------------------------------------------
    df_state_ages = df_demo[
        (df_demo["district_code"] == 0)
        & (df_demo["residence_type"] == "Total")
        & (~df_demo["is_summary_age_group"])
    ].copy()

    fig2, ax2 = plt.subplots(figsize=(11, 5.5))
    x_indices = np.arange(len(df_state_ages))
    width = 0.38

    ax2.bar(x_indices - width / 2, df_state_ages["divorced_males"], width, label="Males", color="#3b82f6")
    ax2.bar(x_indices + width / 2, df_state_ages["divorced_females"], width, label="Females", color="#ec4899")

    ax2.set_title("Recorded Divorced Population by Age Bracket and Sex (Census of India 2011, Tamil Nadu)", fontsize=13, fontweight="bold", pad=12)
    ax2.set_xlabel("Age Group Bracket", fontsize=11)
    ax2.set_ylabel("Number of Individuals", fontsize=11)
    ax2.set_xticks(x_indices)
    ax2.set_xticklabels(df_state_ages["age_group"], rotation=45, ha="right")
    ax2.legend(title="Biological Sex", frameon=True)
    ax2.grid(True, linestyle=":", alpha=0.6)
    plt.tight_layout()
    fig2.savefig(fig_dir / "figure_2_demographic_age_sex_disparity.png", dpi=300)
    plt.close(fig2)

    # ---------------------------------------------------------
    # Figure 3: District-Wise Caseload Distribution
    # ---------------------------------------------------------
    df_family_dist = (
        df_court_dist[df_court_dist["category_scope"] == "matrimonial_broad"]
        .groupby("district_standardized")["cases_pending"]
        .sum()
        .reset_index()
        .sort_values(by="cases_pending", ascending=True)
    )

    fig3, ax3 = plt.subplots(figsize=(8, 10))
    ax3.barh(df_family_dist["district_standardized"], df_family_dist["cases_pending"], color="#0284c7")
    ax3.set_title("Active Matrimonial Caseload by District Court Complex (Tamil Nadu)", fontsize=12, fontweight="bold", pad=12)
    ax3.set_xlabel("Pending Cases", fontsize=10)
    ax3.grid(True, linestyle=":", alpha=0.6)
    plt.tight_layout()
    fig3.savefig(fig_dir / "figure_3_district_pendency_distribution.png", dpi=300)
    plt.close(fig3)

    # ---------------------------------------------------------
    # Figure 4: Pendency Survival Curve S(t)
    # ---------------------------------------------------------
    lab = StatisticalLab()
    exp6 = lab.experiment_6_case_duration_survival()
    s_vals = exp6["survival_function_estimates"]

    t_thresholds = [0, 1, 3, 5, 10]
    s_probs = [
        s_vals["S_greater_than_0_years"],
        s_vals["S_greater_than_1_year"],
        s_vals["S_greater_than_3_years"],
        s_vals["S_greater_than_5_years"],
        s_vals["S_greater_than_10_years"],
    ]

    fig4, ax4 = plt.subplots(figsize=(8, 5))
    ax4.step(t_thresholds, s_probs, where="post", color="#4f46e5", linewidth=2.5, marker="o")
    ax4.axhline(0.5, color="#64748b", linestyle=":", label="Median Survival Horizon (S = 0.5)")
    ax4.axvline(1.9, color="#ef4444", linestyle="--", label="Estimated Median Pendency = 1.9 Years")

    ax4.set_title("Empirical Pendency Survival Curve S(t) — Tamil Nadu Family Courts", fontsize=12, fontweight="bold", pad=12)
    ax4.set_xlabel("Duration Threshold t (Years)", fontsize=10)
    ax4.set_ylabel("Probability of Remaining Active S(t)", fontsize=10)
    ax4.set_ylim(0, 1.05)
    ax4.legend(loc="upper right", frameon=True)
    ax4.grid(True, linestyle=":", alpha=0.6)
    plt.tight_layout()
    fig4.savefig(fig_dir / "figure_4_pendency_survival_curve.png", dpi=300)
    plt.close(fig4)

    # ---------------------------------------------------------
    # Tables Export
    # ---------------------------------------------------------
    # Table 1: District Marital Disruption Rates
    dist_total = df_demo[
        (df_demo["district_code"] != 0)
        & (df_demo["residence_type"] == "Total")
        & (df_demo["age_group"] == "All ages")
    ].copy()
    dist_total["divorce_rate_per_1000"] = (dist_total["divorced_persons"] / dist_total["total_population_persons"]) * 1000
    dist_total["separation_rate_per_1000"] = (dist_total["separated_persons"] / dist_total["total_population_persons"]) * 1000
    dist_total["female_to_male_ratio"] = dist_total["divorced_females"] / dist_total["divorced_males"].replace(0, 1)

    t1_df = dist_total[
        ["district_standardized", "total_population_persons", "divorced_persons", "separated_persons", "divorce_rate_per_1000", "separation_rate_per_1000", "female_to_male_ratio"]
    ].sort_values(by="divorce_rate_per_1000", ascending=False)
    t1_df.to_csv(tab_dir / "table_1_district_divorce_rates.csv", index=False)

    # Table 2: Multi-Year Court Workload Time Series
    df_court_ts.to_csv(tab_dir / "table_2_court_workload_time_series.csv", index=False)

    # Table 3: Forecasting Evaluation Benchmarks
    forecaster = WorkloadForecaster()
    f_rep = forecaster.run_all()
    rows_m = []
    for model_name, res in f_rep["filings_forecast"]["model_evaluations"].items():
        rows_m.append({
            "target": "cases_filed",
            "model_architecture": res["name"],
            "mae": res["metrics"]["mae"],
            "rmse": res["metrics"]["rmse"],
            "mape_pct": res["metrics"]["mape_pct"],
        })
    pd.DataFrame(rows_m).to_csv(tab_dir / "table_3_model_evaluation_benchmarks.csv", index=False)

    print("All research figures and tables generated successfully in outputs/figures/ and outputs/tables/.")


if __name__ == "__main__":
    generate_all_artifacts()
