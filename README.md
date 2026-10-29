# Analyzing Divorce Cases in Tamil Nadu
### Judicial Trends, Demographic Patterns, Statistical Inference, and Predictive Analytics

A research-grade Python web application and scientific laboratory investigating marital dissolution and matrimonial adjudication across Tamil Nadu, India.

---

## 🌟 Key Research Highlights

- **Demographic Stock (Census 2011 Table C-02):**
  - **Tamil Nadu Population:** 72,147,030
  - **Recorded Divorced Individuals:** 62,948 (0.87 per 1,000 population)
  - **Recorded Separated Individuals:** 398,284 (5.52 per 1,000 population)
  - **Gender Asymmetry:** Female-to-Male divorced ratio is **2.54 : 1** (Odds Ratio = 2.53, $p < 10^{-15}$).
- **Judicial Caseload (DoJ / Lok Sabha / NJDG):**
  - **Functional Family Courts:** 40 courts across Tamil Nadu.
  - **Active Pending Backlog:** 31,655 cases (as of 2024).
  - **Annual New Filings:** ~34,120 petitions instituted annually.
  - **COVID-19 Disruption:** 2020 experienced a -37.8% filing drop and an immediate 13.3% surge in pending cases.
  - **Median Pendency:** 61.4% of cases resolve within 3 years (empirical median duration = 1.9 years).
- **Predictive Forecaster:**
  - Evaluated on chronological test holdout (2023–2024). ARIMA(1, 1, 0) selected as best model (Holdout MAPE = 8.01%).
  - 2025 Projected Filings: **34,232** cases (95% PI: [25,713, 42,752]).
- **Ethical Governance & Privacy:**
  - Individual court-outcome probability deployment is **strictly withheld**; evaluation research pipeline is verified without temporal feature leakage.
  - Public reflection questionnaire operates 100% in volatile memory; domestic violence indicators trigger automated safety escalation to **181 Women Helpline** and **112 ERSS**.

---

## 🚀 Quickstart & Installation

### 1. Clone & Setup Environment
Ensure Python 3.10+ is installed:
```bash
# Verify Python version
python --version

# Install dependencies
pip install -r requirements.txt
```

### 2. Run Automated Test Suite
Execute the full testing matrix (40 unit, data quality, model validation, UI, and integration tests):
```bash
pytest
```

### 3. Launch the Interactive Web Application
Start the Streamlit portal:
```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501`.

---

## 📂 Repository Directory Layout

```text
Divorse_Case_TN/
├── app.py                            # Streamlit multi-page application entrypoint
├── requirements.txt                  # Reproducible Python dependencies
├── pyproject.toml                    # Build system & pytest configuration
├── .gitignore                        # Git ignore (excludes cache, venv, chat_history)
├── .env.example                      # Template environment variables
├── config/
│   ├── settings.yaml                 # Runtime settings, paths, seeds
│   └── source_registry.yaml          # Official source registry & SHA-256 hashes
├── data/
│   ├── raw/                          # Unmodified official downloads (Census XLS)
│   ├── processed/                    # Cleaned Parquet and CSV datasets
│   └── metadata/                     # Machine-readable JSON data quality reports
├── src/
│   ├── geography/                    # DistrictCrosswalk (32 to 38 districts)
│   ├── cleaning/                     # Census & court normalization pipelines
│   ├── statistics/                   # StatisticalLab (Experiments 1 to 7)
│   ├── models/                       # WorkloadForecaster, OutcomePredictionPipeline
│   └── assessment/                   # Privacy-preserving reflection & legal guide
├── tests/
│   ├── unit/                         # Unit tests (geography, stats, assessment)
│   ├── data_quality/                 # Ingestion integrity & reconciliation tests
│   ├── model_validation/             # Feature leakage audits & forecast checks
│   ├── integration/                  # End-to-end data & model pipeline tests
│   └── ui/                           # Application compilation & smoke tests
├── docs/                             # Exhaustive technical documentation & monograph
└── outputs/
    └── reports/                      # Exported experimental and model JSON reports
```

---

## 🔄 Rebuilding Data Artifacts from Raw Sources

To reprocess raw data files and re-generate processed datasets:
```bash
python -c "from src.cleaning.demographic_cleaner import DemographicCleaner; DemographicCleaner().save_processed()"
python -c "from src.cleaning.court_cleaner import CourtCleaner; CourtCleaner().save_processed()"
python -c "from src.statistics.statistical_lab import StatisticalLab; StatisticalLab().export_results()"
python -c "from src.models.workload_forecasting import WorkloadForecaster; WorkloadForecaster().run_all()"
python -c "from src.models.outcome_prediction import OutcomePredictionPipeline; OutcomePredictionPipeline().run_pipeline()"
```

---

## ⚖️ Legal & Ethical Disclaimers

1. **Not Legal Advice:** The legal information and procedural flowcharts provided in this portal are educational summaries derived from the *Hindu Marriage Act, 1955*, the *Special Marriage Act, 1954*, the *Family Courts Act, 1984*, and reported Supreme Court precedents. They do not constitute formal legal representation or advice.
2. **Not Clinical Therapy:** The Relationship Reflection questionnaire is a non-diagnostic self-reflection tool. It does not calculate a probability of divorce or diagnose psychological conditions.
3. **Emergency Support:** If you or someone you know is in immediate danger or facing domestic abuse, contact the Tamil Nadu 24/7 Women Helpline at **181** or the National Emergency Service at **112**.
