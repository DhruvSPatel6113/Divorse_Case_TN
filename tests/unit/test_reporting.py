"""
Unit tests for research artifact reporting and figure generation.
"""

from pathlib import Path
import pytest
from src.reporting.generate_figures import generate_all_artifacts
from src.reporting.generate_ieee_docx import build_ieee_word_document


def test_generate_figures_and_tables():
    """Verify that reporting figures and summary tables exist and are non-empty."""
    generate_all_artifacts()

    fig_dir = Path("outputs/figures")
    tab_dir = Path("outputs/tables")

    assert (fig_dir / "figure_1_judicial_trends_covid.png").exists()
    assert (fig_dir / "figure_2_demographic_age_sex_disparity.png").exists()
    assert (fig_dir / "figure_3_district_pendency_distribution.png").exists()
    assert (fig_dir / "figure_4_pendency_survival_curve.png").exists()

    assert (tab_dir / "table_1_district_divorce_rates.csv").exists()
    assert (tab_dir / "table_2_court_workload_time_series.csv").exists()
    assert (tab_dir / "table_3_model_evaluation_benchmarks.csv").exists()


def test_generate_ieee_docx():
    """Verify IEEE Word Document (.docx) is generated with non-zero size."""
    docx_path = Path("outputs/reports/IEEE_Conference_Paper_Tamil_Nadu_Divorce_Analytics.docx")
    assert docx_path.exists()
    assert docx_path.stat().st_size > 50000  # should be around 780KB with figures
