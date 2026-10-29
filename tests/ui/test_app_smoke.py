"""
UI and Application Smoke Tests.
"""

import py_compile
from pathlib import Path
import pytest
from app import load_all_datasets, PAGES


def test_app_syntax():
    """Verify app.py compiles cleanly without syntax errors."""
    app_path = Path("app.py")
    assert app_path.exists()
    py_compile.compile(str(app_path), doraise=True)


def test_app_pages_list():
    """Verify all 8 required pages are configured."""
    required = [
        "Overview",
        "Court Activity",
        "Demographics",
        "Statistical Laboratory",
        "Court Outcome Research",
        "Workload Forecasting",
        "Relationship Reflection & Divorce Process Guide",
        "Data & Methodology",
    ]
    assert PAGES == required


def test_load_all_datasets():
    """Verify core dataset loader initializes without exceptions."""
    df_demo, df_court_ts, df_court_dist, stat_results, forecast_results, outcome_results = load_all_datasets()

    assert len(df_demo) == 1980
    assert len(df_court_ts) >= 7
    assert len(df_court_dist) > 0
    assert len(stat_results) == 7
    assert "filings_forecast" in forecast_results
    assert "pendency_forecast" in forecast_results
    assert "candidate_model_results" in outcome_results


def test_all_statistical_lab_keys_present():
    """Verify that statistical lab dictionary contains all 7 experiment keys used by the UI."""
    from src.statistics.statistical_lab import StatisticalLab
    lab = StatisticalLab()
    results = lab.run_all_experiments()

    assert "exp_1_demographic" in results
    assert "exp_2_judicial_trends" in results
    assert "exp_3_inferential" in results
    assert "exp_4_count_regression" in results
    assert "exp_5_association" in results
    assert "exp_6_duration" in results
    assert "exp_7_limitations" in results

