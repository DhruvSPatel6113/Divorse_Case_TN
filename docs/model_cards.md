# Model Cards

This document provides formal model cards for all predictive models developed in the project in accordance with Section 12.E.

---

### Model Card 1: Family Court Workload Forecaster (ARIMA & Holt-Winters)

#### Model Details
- **Developer:** Tamil Nadu Divorce Analysis Autonomous Research Engineering System.
- **Model Type:** Time-series Autoregressive Integrated Moving Average (ARIMA(1, 1, 0)) and Holt Linear Exponential Smoothing.
- **Version:** 1.0.0 (Release 2026).
- **License:** Open Academic / Research Use.

#### Intended Use
- **Primary Use:** Forecasting aggregate annual filings and pending caseloads across Tamil Nadu Family Courts to assist judicial administration, budgetary allocation, and infrastructure planning.
- **Out-of-Scope / Prohibited Uses:** Must **NOT** be applied to individual court cases. A macro forecast does not predict the outcome, duration, or probability of any individual litigant's case.

#### Training Data & Evaluation
- **Data Source:** Lok Sabha Unstarred Question Returns & Department of Justice Family Courts Dashboard (2018–2024).
- **Split Strategy:** Strict chronological split: Training on 2018–2022; Evaluation on holdout test set (2023–2024).
- **Performance Metrics (Cases Filed):**
  - Holdout MAE: **2,724.13** cases.
  - Holdout RMSE: **2,804.81** cases.
  - Holdout MAPE: **8.01%**.
  - Compared against Naive Baseline (MAE = 2,745.0, MAPE = 8.08%) and Exponential Smoothing (MAE = 7,224.06, MAPE = 21.26%).
- **2025–2026 Projections:**
  - 2025 Filings: **34,232** (80% PI: [28,668, 39,796]; 95% PI: [25,713, 42,752]).
  - 2026 Filings: **34,232** (80% PI: [26,364, 42,100]; 95% PI: [22,185, 46,279]).

---

### Model Card 2: Historical Court Outcome Research Pipeline

#### Model Details
- **Model Architectures Evaluated:** Most-Frequent-Class Baseline, Regularized L2 Logistic Regression, Decision Tree, Random Forest Classifier.
- **Intended Use:** Academic investigation of class balance, pre-filing feature correlations, and evaluation metrics in family court proceedings.
- **Target Variable:** Multi-class disposition: `DECREE_GRANTED`, `PETITION_DISMISSED`, `PETITION_WITHDRAWN`, `RESOLVED_MEDIATION`.
- **Pre-filing Feature Space:** Petitioner type, marriage duration, minor children indicator, legal statute (HMA 13(1), HMA 13B, SMA 27, Divorce Act), counsel representation, court tier, residence.

#### Leakage Audit & Governance Protocol
- **Leakage Verification:** 100% verified. All post-filing signals (`disposal_date`, `final_order_date`, `interim_maintenance_ordered`) are strictly excluded.
- **Evaluation Performance (Holdout Set, Stratified):**
  - Most Frequent Baseline: Accuracy = 0.563, Balanced Accuracy = 0.250, Macro F1 = 0.180.
  - Random Forest: Accuracy = 0.567, Balanced Accuracy = 0.253, Macro F1 = 0.190.
- **Deployment Status:** **INDIVIDUAL DEPLOYMENT WITHHELD**.
  - Reason: Unvalidated individualized probability predictions are prohibited under legal-tech governance standards. Real eCourts microdata is protected by CAPTCHAs. The evaluation pipeline exists for research methodology benchmarking only.
