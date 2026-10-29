"""
Data Quality and Ingestion Tests for Demographic Dataset (Census 2011 Table C-02).
"""

import json
from pathlib import Path
import pandas as pd
import pytest

from src.cleaning.demographic_cleaner import DemographicCleaner, EXPECTED_SHA256


def test_census_raw_file_integrity():
    cleaner = DemographicCleaner()
    assert cleaner.raw_file_path.exists()
    computed_sha = cleaner.compute_sha256()
    assert computed_sha.lower() == EXPECTED_SHA256.lower()


def test_demographic_reconciliation_zero_discrepancies():
    cleaner = DemographicCleaner()
    df, report = cleaner.process()

    assert report["sha256_integrity_verified"] is True
    assert report["reconciliation_discrepancies"] == 0
    assert report["geographic_coverage"]["district_count"] == 32
    assert report["dimensions_evaluated"]["completeness"] == 1.0
    assert report["dimensions_evaluated"]["validity"] == 1.0


def test_demographic_state_totals():
    cleaner = DemographicCleaner()
    df, report = cleaner.process()

    totals = report["reconciled_state_totals"]
    assert totals["total_population"] == 72147030
    assert totals["divorced_persons"] == 62948
    assert totals["separated_persons"] == 398284
    assert totals["divorced_males"] + totals["divorced_females"] == totals["divorced_persons"]
    assert totals["separated_males"] + totals["separated_females"] == totals["separated_persons"]


def test_demographic_nonnegative_counts():
    cleaner = DemographicCleaner()
    df, _ = cleaner.process()

    numeric_cols = [
        "total_population_persons",
        "never_married_persons",
        "currently_married_persons",
        "widowed_persons",
        "separated_persons",
        "divorced_persons",
    ]
    for col in numeric_cols:
        assert (df[col] >= 0).all(), f"Found negative counts in {col}"


def test_demographic_saved_artifacts():
    cleaner = DemographicCleaner()
    csv_p, parq_p, rep_p = cleaner.save_processed()

    assert csv_p.exists()
    assert rep_p.exists()

    df_loaded = pd.read_csv(csv_p)
    assert len(df_loaded) == 1980
    assert "district_standardized" in df_loaded.columns
    assert "divorced_separated_persons" in df_loaded.columns
