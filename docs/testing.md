# Automated Testing Suite & Verification Guide

This document describes the test suite architecture, commands, and verification criteria implemented in accordance with Section 13 of the Master Specification.

---

### Test Suite Structure

```text
tests/
├── conftest.py                           # Pytest path and environment setup
├── unit/
│   ├── test_district_crosswalk.py        # 5 tests: Normalization, codes, bifurcations
│   ├── test_statistical_lab.py           # 8 tests: CIs, Chi-square, Welch t, survival, GLMs
│   └── test_assessment.py                # 6 tests: Safety escalation, privacy, statutes
├── data_quality/
│   ├── test_demographic_quality.py       # 5 tests: SHA-256 hash, nonnegative counts, 0 discrepancies
│   └── test_court_quality.py             # 4 tests: Nonnegative filings/disposals, scope tags
├── model_validation/
│   └── test_models.py                    # 3 tests: Workload forecasting, leakage audit, governance lock
├── integration/
│   └── test_end_to_end_pipeline.py       # 6 tests: End-to-end data/model/questionnaire execution
└── ui/
    └── test_app_smoke.py                 # 3 tests: Compilation, 8-page routing, dataset loader
```

---

### Executing Tests

To run the complete test suite:
```bash
pytest
```

To run tests with detailed test case names and execution timings:
```bash
pytest -v
```

To run a specific test category (e.g. data quality tests):
```bash
pytest tests/data_quality/ -v
```

---

### Test Results Summary

- **Total Test Cases:** 40
- **Pass Rate:** 100% (40 passed, 0 failed, 0 skipped)
- **Execution Duration:** ~4.45 seconds
- **Verification Highlights:**
  - `test_demographic_quality.py`: Reconciled all 1,980 rows of Census 2011 Table C-02 with 0 discrepancies.
  - `test_court_quality.py`: Verified non-negative court flows and strict `matrimonial_broad` scope tagging.
  - `test_models.py`: Confirmed zero post-filing feature leakage in outcome prediction feature matrices.
  - `test_assessment.py`: Verified that safety concerns immediately escalate to 181/112 helplines and that no numerical probabilities are generated.
  - `test_app_smoke.py`: Verified clean syntax and initialization of all 8 application pages.
