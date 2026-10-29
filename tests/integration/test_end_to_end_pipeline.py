"""
Comprehensive End-to-End Integration Tests.

Validates the full workflow from raw data ingestion to quality checks,
statistical calculations, predictive modeling, questionnaire flows,
and artifact export per Section 13.B.
"""

import json
from pathlib import Path
import pandas as pd
import pytest

from src.cleaning.demographic_cleaner import DemographicCleaner
from src.cleaning.court_cleaner import CourtCleaner
from src.statistics.statistical_lab import StatisticalLab
from src.models.workload_forecasting import WorkloadForecaster
from src.models.outcome_prediction import OutcomePredictionPipeline
from src.assessment.questionnaire import QuestionnaireManager, QuestionnaireResponse
from src.assessment.relationship_reflection import RelationshipReflectionEngine
from src.assessment.legal_information import LegalInformationGuide


def test_pipeline_1_demographic_raw_to_quality_report():
    """1 & 2: Raw Census XLS -> Cleaner -> Normalized Parquet & JSON Quality Report."""
    cleaner = DemographicCleaner()
    csv_p, parq_p, rep_p = cleaner.save_processed()

    assert csv_p.exists()
    assert parq_p.exists()
    assert rep_p.exists()

    with open(rep_p) as f:
        rep = json.load(f)
    assert rep["sha256_integrity_verified"] is True
    assert rep["reconciliation_discrepancies"] == 0
    assert rep["geographic_coverage"]["district_count"] == 32


def test_pipeline_2_court_to_quality_report():
    """Court raw records -> Normalized CSV & Parquet with category scopes."""
    cleaner = CourtCleaner()
    p_ts, p_dist, p_parq, p_rep = cleaner.save_processed()

    assert p_ts.exists()
    assert p_dist.exists()
    assert p_rep.exists()

    df_ts = pd.read_csv(p_ts)
    assert (df_ts["category_scope"] == "matrimonial_broad").all()


def test_pipeline_3_statistical_laboratory_end_to_end():
    """3: Clean data -> Statistical calculations -> Structured JSON report."""
    lab = StatisticalLab()
    out_p = lab.export_results()

    assert out_p.exists()
    with open(out_p) as f:
        results = json.load(f)

    assert "exp_1_demographic" in results
    assert "exp_2_judicial_trends" in results
    assert "exp_3_inferential" in results
    assert "exp_4_count_regression" in results
    assert "exp_5_association" in results
    assert "exp_6_duration" in results
    assert "exp_7_limitations" in results


def test_pipeline_4_workload_forecasting_end_to_end():
    """4: Time series -> Chronological split -> Baseline & ARIMA -> Predictions & Intervals."""
    forecaster = WorkloadForecaster()
    rep = forecaster.run_all()

    filings = rep["filings_forecast"]
    assert filings["best_model"] in filings["model_evaluations"]
    assert "projection_2025" in filings["future_projections"]
    assert "projection_2026" in filings["future_projections"]


def test_pipeline_5_outcome_prediction_leakage_and_governance():
    """5: Case research data -> Leakage audit -> Model training -> Governance restriction."""
    pipeline = OutcomePredictionPipeline()
    rep = pipeline.run_pipeline()

    assert rep["leakage_audit_passed"] is True
    assert rep["deployment_governance_status"]["individual_probability_deployment_allowed"] is False


def test_pipeline_6_questionnaire_and_reflection():
    """6 & 7: Questionnaire answers -> In-memory reflection & verified legal guidance."""
    q_mgr = QuestionnaireManager()
    ref_engine = RelationshipReflectionEngine()
    legal_guide = LegalInformationGuide()

    resp = QuestionnaireResponse(
        query_context="relationship_concerns",
        concerns=["Communication breakdown", "In-laws / Extended family interference"],
        discussion_safety="somewhat_tense",
        user_goal="reconciliation_pathways",
    )
    assert q_mgr.validate_safety_flags(resp) is False

    ref_rep = ref_engine.generate_reflection_report(resp)
    assert len(ref_rep["reflection_themes"]) == 2
    assert "probability" not in ref_rep

    legal_rep = legal_guide.get_comprehensive_guide("hindu_marriage_act", "mutual_consent")
    assert "Hindu Marriage Act, 1955" in legal_rep["statutory_framework"]["statute_name"]
    assert len(legal_rep["procedural_track"]["stages"]) == 5
