# Directory Guide

This document explains the organization and responsibilities of every directory in the project repository, in accordance with Section 12.B of the Master Specification.

---

### Root Directory (`/`)
- **Responsibility:** Contains the top-level application entrypoint (`app.py`), package definitions (`pyproject.toml`, `requirements.txt`), version control configuration (`.gitignore`), and environment templates (`.env.example`).
- **Dependencies:** Serves as the Python execution root (`PYTHONPATH=.`).

---

### `config/`
- **Responsibility:** Stores static configuration, source provenance metadata, and operational parameters.
- **Key Files:**
  - `config/settings.yaml`: Runtime constants, file paths, model seeds, and privacy flags.
  - `config/source_registry.yaml`: Official source registry tracking publishers, URLs, access status, SHA-256 hashes, and temporal coverage.
- **Allowed Contents:** YAML or JSON configuration files only. No runtime data or secrets.

---

### `data/`
- **Responsibility:** Data tier separating raw, interim, processed, and metadata artifacts.
- **Subdirectories:**
  - `data/raw/`: Read-only, unmodified official downloads (e.g. `DDW-3300C-02-fer3-MDDS.xls`). Must remain bit-for-bit identical to source.
  - `data/interim/`: Intermediate staging files during multi-step transforms.
  - `data/processed/`: Normalized, validated datasets in Parquet and CSV formats (`demographic_tn_2011.parquet`, `court_time_series_tn.csv`, `court_districts_pendency_tn.csv`).
  - `data/metadata/`: Machine-readable data quality reports, checksum verifications, and reconciliation audits (`demographic_quality_report.json`, `court_quality_report.json`).

---

### `src/`
- **Responsibility:** Core Python business logic, ETL pipelines, statistical routines, models, and public-facing assessment modules.
- **Subdirectories:**
  - `src/geography/`: Geographic standardization, 2011 Census 32-district codes, and 2019-2020 administrative bifurcation tracking (`district_crosswalk.py`).
  - `src/ingestion/`: Permitted data acquisition routines and raw file loaders.
  - `src/cleaning/`: Normalization, deduplication, nonnegative count validation, and schema enforcement (`demographic_cleaner.py`, `court_cleaner.py`).
  - `src/statistics/`: Scientific statistical laboratory implementing Experiments 1 to 7 (`statistical_lab.py`).
  - `src/models/`: Predictive models, macro workload forecasters (`workload_forecasting.py`), court-outcome research pipelines with feature-leakage audits (`outcome_prediction.py`), and evaluation metrics (`evaluation.py`).
  - `src/assessment/`: Privacy-preserving public self-reflection questionnaire (`questionnaire.py`, `relationship_reflection.py`) and verified statutory guides (`legal_information.py`).
  - `src/utils/`: Helper utilities and shared functions.

---

### `tests/`
- **Responsibility:** Automated testing suite covering the complete verification matrix.
- **Subdirectories:**
  - `tests/unit/`: Logic tests for district crosswalks, statistical formulas (Wilson CIs, Chi-square, t-tests), and questionnaire branching (`test_district_crosswalk.py`, `test_statistical_lab.py`, `test_assessment.py`).
  - `tests/data_quality/`: Integrity tests for SHA-256 checksums, nonnegative counts, and stock-flow reconciliations (`test_demographic_quality.py`, `test_court_quality.py`).
  - `tests/model_validation/`: Safeguard tests verifying zero feature leakage, metric calculations, and governance locks (`test_models.py`).
  - `tests/integration/`: End-to-end integration tests chaining ingestion, normalization, modeling, and output exports (`test_end_to_end_pipeline.py`).
  - `tests/ui/`: Application compilation, page routing, and dataset loader smoke tests (`test_app_smoke.py`).

---

### `docs/`
- **Responsibility:** Exhaustive technical documentation, continuous build logging, architecture diagrams, data dictionaries, methodology notes, model cards, and the comprehensive research report.

---

### `outputs/`
- **Responsibility:** Exported research artifacts, figures, tables, and machine-readable JSON summaries.
- **Subdirectories:**
  - `outputs/figures/`: Static and interactive visualizations.
  - `outputs/tables/`: Exported summary CSV tables.
  - `outputs/reports/`: Full experimental and model evaluation JSON records (`statistical_lab_results.json`, `workload_forecast_report.json`, `outcome_prediction_report.json`).

---

### `chat_history/`
- **Responsibility:** Project-wise chat history and developer interaction records.
- **Security & Privacy:** Strictly ignored in `.gitignore` to ensure it resides only on local machine storage and is never uploaded or shared remotely.
