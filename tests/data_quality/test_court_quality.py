"""
Data Quality and Ingestion Tests for Court Datasets.
"""

import json
from pathlib import Path
import pandas as pd
import pytest

from src.cleaning.court_cleaner import CourtCleaner


def test_court_time_series_nonnegative_counts():
    cleaner = CourtCleaner()
    df_ts, _, _ = cleaner.process()

    assert (df_ts["cases_filed"] > 0).all()
    assert (df_ts["cases_disposed"] > 0).all()
    assert (df_ts["cases_pending"] > 0).all()
    assert (df_ts["functional_courts"] >= 30).all()


def test_court_category_scopes():
    cleaner = CourtCleaner()
    df_ts, df_dist, report = cleaner.process()

    # Time series must be marked matrimonial_broad
    assert (df_ts["category_scope"] == "matrimonial_broad").all()

    # District data must only have valid scopes
    allowed = {"matrimonial_broad", "all_cases", "divorce_specific", "unknown"}
    assert set(df_dist["category_scope"]).issubset(allowed)


def test_court_district_coverage():
    cleaner = CourtCleaner()
    _, df_dist, report = cleaner.process()

    assert report["district_coverage_count"] == 32
    assert "Chennai" in df_dist["district_standardized"].values
    assert "Coimbatore" in df_dist["district_standardized"].values
    assert "Madurai" in df_dist["district_standardized"].values


def test_court_saved_artifacts():
    cleaner = CourtCleaner()
    p_ts, p_dist, _, p_rep = cleaner.save_processed()

    assert p_ts.exists()
    assert p_dist.exists()
    assert p_rep.exists()

    df_ts_read = pd.read_csv(p_ts)
    assert len(df_ts_read) >= 7
    assert "clearance_rate_pct" in df_ts_read.columns
