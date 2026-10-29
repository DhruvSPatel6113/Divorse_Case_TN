# File Guide

This document maintains a comprehensive, file-by-file inventory of project-owned files in accordance with Section 12.C of the Master Specification.

---

### Root Configuration & Entrypoints

| File | Purpose | Key Functions / Classes | Inputs / Outputs | Tests |
| :--- | :--- | :--- | :--- | :--- |
| `app.py` | Multi-page Streamlit interactive research GUI | `main()`, `load_all_datasets()`, `render_overview()`, `render_court_activity()`, etc. | In: Processed CSVs/Parquet<br>Out: Interactive web UI | `tests/ui/test_app_smoke.py` |
| `pyproject.toml` | Build system and pytest configuration | `[project]`, `[tool.pytest.ini_options]` | Package metadata | pytest execution |
| `requirements.txt` | Reproducible pip dependency definitions | Package list | Pip installer | Pip check |
| `.gitignore` | Excludes temporary caches, virtualenvs, and local chat history | Ignore rules | Git VCS | Git status |
| `.env.example` | Environment variable template | Environment names | Setup reference | N/A |
| `README.md` | Top-level project documentation and quickstart instructions | User guide | Markdown viewer | Visual inspection |

---

### Core Source Code (`src/`)

| File | Purpose | Key Functions / Classes | Inputs / Outputs | Tests |
| :--- | :--- | :--- | :--- | :--- |
| `src/geography/district_crosswalk.py` | District standardization and split tracking (32 to 38 districts) | `DistrictCrosswalk`, `standardize()`, `get_split_details()`, `get_census_code()` | In: Raw district strings<br>Out: Standardized names & split metadata | `tests/unit/test_district_crosswalk.py` |
| `src/cleaning/demographic_cleaner.py` | Parses Census 2011 Table C-02, verifies SHA-256, reconciles counts | `DemographicCleaner`, `process()`, `save_processed()` | In: `DDW-3300C-02-fer3-MDDS.xls`<br>Out: Parquet, CSV, Quality JSON | `tests/data_quality/test_demographic_quality.py` |
| `src/cleaning/court_cleaner.py` | Standardizes judicial time series and district pendency age profiles | `CourtCleaner`, `build_time_series_dataset()`, `save_processed()` | In: Verified official court records<br>Out: CSV, Parquet, Quality JSON | `tests/data_quality/test_court_quality.py` |
| `src/statistics/statistical_lab.py` | Implements Experiments 1–7 (Demographics, Trends, Inference, GLMs, Survival) | `StatisticalLab`, `wilson_score_interval()`, `experiment_1` to `experiment_7` | In: Cleaned datasets<br>Out: Comprehensive JSON results | `tests/unit/test_statistical_lab.py` |
| `src/models/evaluation.py` | Hand-verifiable metric calculations for regression and classification | `evaluate_forecast()`, `evaluate_classification()` | In: `y_true`, `y_pred`, `y_prob`<br>Out: MAE, RMSE, Macro F1, Brier | `tests/model_validation/test_models.py` |
| `src/models/workload_forecasting.py` | Macro court workload forecasting with baseline and ARIMA models | `WorkloadForecaster`, `fit_and_evaluate()`, `run_all()` | In: Annual court filings series<br>Out: Projections & intervals | `tests/model_validation/test_models.py` |
| `src/models/outcome_prediction.py` | Outcome research pipeline with strict feature-leakage audit | `OutcomePredictionPipeline`, `verify_feature_leakage()`, `evaluate_models()` | In: Pre-filing feature matrices<br>Out: Classifier benchmarks | `tests/model_validation/test_models.py` |
| `src/assessment/questionnaire.py` | Privacy-preserving questionnaire schema and validation | `QuestionnaireManager`, `QuestionnaireResponse`, `validate_safety_flags()` | In: User selections<br>Out: In-memory structured response | `tests/unit/test_assessment.py` |
| `src/assessment/relationship_reflection.py` | Non-diagnostic self-reflection engine with safety escalation | `RelationshipReflectionEngine`, `generate_reflection_report()` | In: `QuestionnaireResponse`<br>Out: Guidance, Helplines | `tests/unit/test_assessment.py` |
| `src/assessment/legal_information.py` | Objective Indian family law procedural guide and case law | `LegalInformationGuide`, `get_statutory_details()`, `get_procedural_track()` | In: Statute and track keys<br>Out: Step-by-step procedures | `tests/unit/test_assessment.py` |
| `src/reporting/generate_figures.py` | Generates publication figures and summary tables in outputs/ | `generate_all_artifacts()` | In: Processed CSVs<br>Out: PNG figures, summary CSV tables | `tests/unit/test_reporting.py` |
| `src/reporting/generate_ieee_docx.py` | Generates publication-grade IEEE Conference paper Word document (.docx) with VIT Vellore affiliation | `build_ieee_word_document()` | In: Figures, tables, metrics<br>Out: Word docx paper | `tests/unit/test_reporting.py` |

---

### Automated Tests (`tests/`)

| File | Purpose | Test Cases |
| :--- | :--- | :--- |
| `tests/conftest.py` | Pytest environment configuration and sys.path setup | Python path resolution |
| `tests/unit/test_district_crosswalk.py` | Verifies district name standardization and split lineage | 5 unit tests |
| `tests/unit/test_reporting.py` | Verifies publication figure, table, and IEEE docx paper artifact generation | 2 unit tests |
| `tests/unit/test_statistical_lab.py` | Verifies statistical formulas, Wilson bounds, GLMs, and Chi-square | 8 unit tests |
| `tests/unit/test_assessment.py` | Verifies safety escalation, non-diagnostic output, and statutory flows | 6 unit tests |
| `tests/data_quality/test_demographic_quality.py` | Verifies Census 2011 SHA-256, nonnegative counts, and 0 discrepancies | 5 quality tests |
| `tests/data_quality/test_court_quality.py` | Verifies court time series integrity and category scope enforcement | 4 quality tests |
| `tests/model_validation/test_models.py` | Verifies feature-leakage prevention, forecast intervals, and governance lock | 3 validation tests |
| `tests/integration/test_end_to_end_pipeline.py` | Verifies end-to-end integration across all modules | 6 integration tests |
| `tests/ui/test_app_smoke.py` | Verifies Streamlit app compilation, page lists, and dataset caching | 3 smoke tests |
