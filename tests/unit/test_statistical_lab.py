"""
Unit tests for Statistical Laboratory (Experiments 1 to 7).
"""

import json
from pathlib import Path
import pytest
from src.statistics.statistical_lab import StatisticalLab, wilson_score_interval


def test_wilson_score_interval():
    low, high = wilson_score_interval(50, 100, 0.95)
    assert 0.0 <= low < 0.5 < high <= 1.0
    assert round(low, 2) == 0.40
    assert round(high, 2) == 0.60

    # Zero count test
    low_zero, high_zero = wilson_score_interval(0, 100, 0.95)
    assert low_zero == 0.0
    assert high_zero > 0.0


def test_experiment_1_demographic():
    lab = StatisticalLab()
    exp1 = lab.experiment_1_demographic_distribution()
    assert "statewide_metrics" in exp1
    assert exp1["statewide_metrics"]["total_population"] == 72147030
    assert exp1["statewide_metrics"]["divorced_count"] == 62948
    assert exp1["statewide_metrics"]["sex_ratio_divorce"]["female_to_male_ratio"] > 2.0


def test_experiment_2_judicial_trends():
    lab = StatisticalLab()
    exp2 = lab.experiment_2_judicial_trends()
    assert "summary_statistics" in exp2
    assert exp2["summary_statistics"]["mean_annual_filings"] > 20000
    assert exp2["covid_impact_2020"]["filing_drop_pct"] < 0  # Drop in 2020


def test_experiment_3_inferential():
    lab = StatisticalLab()
    exp3 = lab.experiment_3_statistical_inference()
    assert exp3["test_1_sex_disparity"]["chi2_statistic"] > 1000
    assert exp3["test_1_sex_disparity"]["p_value"] < 0.001
    assert exp3["test_1_sex_disparity"]["odds_ratio_female_to_male"] > 2.0
    assert "test_2_rural_urban_comparison" in exp3


def test_experiment_4_regression():
    lab = StatisticalLab()
    exp4 = lab.experiment_4_count_regression()
    assert "poisson_glm" in exp4
    assert "negative_binomial_glm" in exp4
    assert exp4["poisson_glm"]["aic"] > 0


def test_experiment_5_association():
    lab = StatisticalLab()
    exp5 = lab.experiment_5_demographic_judicial_association()
    assert "correlation_analysis" in exp5
    assert -1.0 <= exp5["correlation_analysis"]["pearson_r"] <= 1.0
    assert "ECOLOGICAL FALLACY WARNING" in exp5["critical_methodological_caveat"]


def test_experiment_6_survival():
    lab = StatisticalLab()
    exp6 = lab.experiment_6_case_duration_survival()
    s_est = exp6["survival_function_estimates"]
    assert s_est["S_greater_than_0_years"] == 1.0
    assert s_est["S_greater_than_1_year"] > s_est["S_greater_than_3_years"]
    assert s_est["S_greater_than_3_years"] > s_est["S_greater_than_5_years"]
    assert s_est["S_greater_than_5_years"] > s_est["S_greater_than_10_years"]


def test_run_all_and_export():
    lab = StatisticalLab()
    out_p = lab.export_results()
    assert out_p.exists()
    with open(out_p) as f:
        data = json.load(f)
    assert len(data) == 7
