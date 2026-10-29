# MASTER AUTONOMOUS BUILD PROMPT
## Analyzing Divorce Cases in Tamil Nadu — Research, Statistics, Machine Learning, and Interactive Web Application

> **Instructions for the autonomous coding agent:** Treat this entire document as the project specification. Begin work immediately. Do not ask the user to rewrite, clarify, or approve routine decisions. Inspect the workspace first, then research, implement, test, document, and iterate until the acceptance criteria are met or a genuine external blocker is reached.

---

## 1. Mission and role

Act as an autonomous senior research engineer, statistician, data scientist, machine-learning engineer, data engineer, full-stack developer, QA engineer, technical writer, and data-governance specialist.

Build a complete, runnable, research-grade web application titled:

**Analyzing Divorce Cases in Tamil Nadu: Judicial Trends, Demographic Patterns, Statistical Inference, and Predictive Analytics**

This is not merely a proposal, UI mockup, notebook, or collection of placeholder files. Deliver a working project that researches official sources, collects permitted data, validates and processes it, runs defensible statistical analyses, trains and evaluates suitable models where possible, presents results through a simple interactive GUI, tests the system automatically, and documents the entire build and research process.

Make routine technical decisions autonomously. Inspect the current workspace before changing anything. Preserve useful existing work. Do not ask for confirmation for ordinary implementation choices.

If a data source is unavailable, a download fails, or a model is not supportable by available data, document the blocker and continue with all other feasible work. Never fabricate observations, invent endpoints, bypass access controls, or represent a placeholder as a completed feature.

## 2. Core research objectives

Build three distinct but integrated areas.

### A. Judicial case analysis

Investigate divorce-related judicial activity in Tamil Nadu, including where verified data permits:

- Divorce petitions instituted/filed.
- Cases disposed of.
- Cases pending.
- Disposal categories and final outcomes.
- Case duration and pendency-age distributions.
- Trends over time.
- District and court-level differences.
- Differences between divorce-specific cases and broader matrimonial, family-court, or all-case statistics.
- Aggregate court workload forecasting.

### B. Demographic analysis

Analyze official marital-status data, including:

- Counts and proportions of people recorded as divorced or separated.
- Distribution by age group, sex, residence, and district where available.
- Geographic and demographic differences.
- Associations between aggregate demographic indicators and judicial activity.
- District-boundary changes and source-definition differences.

A census count of people recorded as divorced is not the same as the number of divorce petitions filed in a particular year. Keep these concepts separate throughout the project.

### C. Predictive and public-facing features

Implement distinct modules for:

1. **Historical court-outcome research:** Estimate defined outcomes for historical cases only if lawful, reliable, sufficiently representative, properly labelled data is available.
2. **Court workload forecasting:** Forecast aggregate filings or pendency if the historical time series supports it.
3. **Relationship reflection and legal-process guide:** Help users understand their concerns, possible pathways, and questions to discuss with qualified professionals.

Do not treat these as interchangeable prediction problems. A workload forecast does not predict the result of a person's case. A relationship questionnaire is not a validated predictor of whether a marriage will end in divorce.

---

## 3. Official data-source discovery

Start with an official-source feasibility audit. Investigate these priority sources:

1. National Judicial Data Grid: https://njdg.ecourts.gov.in/
2. eCourts Services: https://services.ecourts.gov.in/ecourtindia_v6/
3. Census of India, Tamil Nadu 2011 C-02 marital-status tables: https://censusindia.gov.in/nada/index.php/catalog/10334
4. Tamil Nadu Open Government Data portal: https://tn.data.gov.in/keywords/Cases
5. India Code: https://www.indiacode.nic.in/

Also investigate relevant official publications from the Department of Justice, Ministry of Law and Justice, National Informatics Centre, Census of India, and Tamil Nadu government departments.

Prefer official sources. Secondary academic publications can inform methods but must not silently replace official observations.

For each source, document:

- Publisher and source name.
- Official URL and exact resource URL.
- Available fields and their definitions.
- Geographic and temporal coverage.
- File format and update frequency.
- Whether data is aggregate or case-level.
- Whether the category is divorce-specific, matrimonial-broad, all-case, or unknown.
- Access restrictions and permitted retrieval method.
- Verification status.
- Retrieval timestamp.
- Raw-file checksum, if downloaded.
- Known limitations and unresolved questions.

Clearly distinguish **verified source**, **successfully retrieved**, **partially retrieved**, **inaccessible**, and **coverage unconfirmed**.

### Data acquisition requirements

- Automate permitted downloads through documented official endpoints.
- Use an API only if its existence, documentation, and terms have been verified.
- Do not assume a dashboard has a bulk API.
- Do not bypass CAPTCHAs, authentication, rate limits, or access controls.
- If automated retrieval is unavailable, implement a documented manual-import workflow and continue.
- Preserve original raw files unmodified.
- Store cleaned data separately from raw data.
- Make ingestion idempotent so reruns do not create duplicate observations.
- Log failures and retry transient failures responsibly.
- Never label synthetic test data as official data.

---

## 4. Data schemas and provenance

Create a documented, consistent data model that preserves source values and their provenance.

### A. Court aggregate dataset

Include fields where available:

- `source_id`
- `source_record_id`
- `state`
- `district_original`
- `district_standardized`
- `court_name`
- `court_level`
- `case_category_original`
- `case_category_standardized`
- `category_scope`
- `period_start`
- `period_end`
- `snapshot_date`
- `cases_filed`
- `cases_disposed`
- `cases_pending`
- `disposal_outcome_category`
- `pendency_age_group`
- `retrieved_at`
- `raw_file_hash`

Allowed values for `category_scope`:

- `divorce_specific`
- `matrimonial_broad`
- `all_cases`
- `unknown`

Never describe general court statistics as divorce statistics.

### B. Demographic dataset

Include:

- `source_id`
- `reference_year`
- `district_original`
- `district_code`
- `district_standardized`
- `residence_type`
- `age_group`
- `sex`
- `marital_status`
- `person_count`
- `source_file`
- `retrieved_at`

Preserve original census labels and document all standardization.

### C. Individual case histories

Create this dataset only when records are lawfully accessible, appropriate for research, and sufficiently complete.

Potential fields:

- Pseudonymous case identifier.
- Court and district identifiers.
- Original and normalized case type.
- Filing date.
- Observation end date.
- Disposal date, if known.
- Status at the observation end.
- Final recorded disposition.
- Outcome source and classification confidence.
- Source reference.
- Extraction timestamp.

Do not collect names, addresses, phone numbers, or unnecessary sensitive personal details. Hashing is pseudonymization, not guaranteed anonymization. Do not combine public records in ways that unnecessarily expose identifiable people.

Never infer an outcome from a case title alone.

### D. District crosswalk

Create a separate crosswalk to manage district splits, mergers, renamings, and differing codes. Include original name/code, standardized name/code, validity period, mapping method, and mapping confidence.

Do not silently merge historical districts into present-day districts.

---

## 5. Automated ingestion, cleaning, and data quality

Implement reusable, testable Python modules for source discovery, retrieval, parsing, normalization, mapping, validation, and persistence.

The pipeline must:

1. Discover or retrieve the source using a permitted method.
2. Record the retrieval timestamp.
3. Save the raw file unchanged.
4. Calculate a SHA-256 checksum.
5. Parse the file.
6. Normalize column names and data types.
7. Map categories and geography.
8. Validate values and definitions.
9. Detect duplicates and conflicting records.
10. Produce a machine-readable quality report.
11. Save cleaned data.
12. Update the source registry and processing logs.

### Validation rules

- Counts must be nonnegative.
- Dates and period boundaries must be valid.
- Required fields must exist.
- Category mappings must be explicit.
- Duplicates must be investigated; do not blindly delete conflicting records.
- Missing values must not automatically become zero.
- Filed, disposed, and pending counts must not be added together as independent cases.
- Conflicting snapshots must be flagged.
- Aggregation definitions must be checked before combining sources.
- Census totals should be reconciled against published totals when possible.
- Missing districts, periods, and categories must be reported.
- Missing observations must be distinguished from true zeros.
- Stock-flow checks may be performed only when source definitions and snapshot intervals align.

Report data-quality dimensions separately: completeness, validity, uniqueness, consistency, geographic coverage, temporal coverage, and freshness.

---

## 6. Statistical analysis laboratory

Implement analyses only when the relevant data exists and assumptions are met.

### Experiment 1: Demographic distribution

Analyze divorced/separated counts and proportions by available age, sex, residence, and district groups. Use valid denominators and label Census 2011 data with its true reference year. Explain that a census status is a population snapshot, not annual divorce incidence.

### Experiment 2: Judicial trends

Analyze filing, disposal, and pendency series. Calculate appropriate descriptive statistics, year-over-year changes where valid, filing-to-disposal comparisons, temporal patterns, and geographic differences where coverage is comparable.

Do not compare incomparable categories, periods, courts, or snapshots without explaining the limitation.

### Experiment 3: Statistical inference

Choose methods according to the data and research question. Potential methods include:

- Confidence intervals for proportions and rates.
- Chi-square tests for suitable categorical comparisons.
- Fisher's exact test for suitable small contingency tables.
- Welch's t-test for appropriate mean comparisons.
- Mann–Whitney or Kruskal–Wallis tests where suitable.
- Correlation analysis with assumptions stated.
- Bootstrap confidence intervals where justified.

For every test, report the research question, null and alternative hypotheses, assumptions, sample size, test statistic, p-value, effect size, and confidence interval where applicable. Correct for multiple comparisons when appropriate. Never equate statistical significance with causation.

### Experiment 4: Count regression

Where appropriate, compare Poisson and negative-binomial regression. Check overdispersion, temporal dependence, structural breaks, and model fit. Use an exposure offset only when its denominator is defensible and aligned with the outcome definition.

### Experiment 5: Demographic/judicial association

Explore aggregate associations using suitable models, uncertainty estimates, and sensitivity analysis. Explicitly state that district-level association cannot establish individual-level behavior or causality.

### Experiment 6: Case duration

If reliable filing and disposition dates exist, implement survival analysis such as Kaplan–Meier, log-rank comparisons, and Cox proportional-hazards models with diagnostics. Define the event, time origin, and observation window. Treat still-pending cases as censored, not completed.

### Experiment 7: Feasibility and limitations

If sample size, labels, coverage, or assumptions are inadequate, explain why the analysis is unavailable. Do not manufacture significance or force every technique into the report.

---

## 7. Historical court-outcome prediction

Create a separate module for research on historical case outcomes.

### Step 1: Define and verify outcome labels

Investigate whether source records reliably distinguish outcomes such as:

- Decree granted.
- Petition dismissed.
- Petition withdrawn.
- Other disposal.
- Pending at observation cutoff.
- Referred to or resolved through mediation/counselling, if explicitly recorded.
- Unknown or ambiguous.

These categories may represent different stages or processes rather than mutually exclusive final outcomes. Define them from verified source documentation and seek legal review when needed.

Do not treat every disposal as divorce approval. Do not equate withdrawal, settlement, dismissal, counselling, and a decree. A counselling referral may be an intermediate event; model it separately only if records support that distinction.

### Step 2: Audit the data

Before training, report usable case count, verified outcome-label count, class distribution, missingness, duplicates, time and court coverage, selection bias, and whether the data represents all cases or a selected subset.

Do not claim to have a useful predictive model if outcome labels are unreliable or the sample is inadequate.

### Step 3: Prevent leakage

Define the exact prediction time. For a model intended to estimate an outcome at filing, do not use disposal date, final outcome, future hearings, later orders, or any feature recorded after filing. Create separate models only when their prediction times and input data are clearly defined.

### Step 4: Train appropriate baselines and candidates

Start with a most-frequent-class baseline. Then compare suitable models such as regularized logistic regression, decision trees, random forests, or gradient-boosted trees where the data supports them.

Use time-based holdouts and group records appropriately to reduce leakage from repeated cases or court-specific patterns. Tune only within training data.

### Step 5: Evaluate honestly

Report confusion matrix, per-class precision and recall, macro F1, balanced accuracy, ROC-AUC when meaningful, precision-recall metrics for imbalanced classes, Brier score and log loss for probabilities, calibration curves, and confidence intervals where feasible.

Check performance over time and across adequately represented groups. High accuracy alone is not sufficient for rare outcomes.

### Step 6: Explain predictions

Use appropriate interpretability methods and distinguish association from causation. Feature importance does not prove that a feature causes an outcome.

### Step 7: Restrict individual use

Historical models are research tools, not judge simulators or legal decision-makers. Do not deploy unsupported individualized court-outcome probabilities.

Only display numerical probabilities if the cohort, target, data provenance, calibration, held-out performance, and applicability are all defensible. State the target population, sample size, time period, uncertainty, and limitations.

If the data does not support the task, implement the evaluation pipeline and display a clear “not available: insufficient validated data” state rather than inventing predictions.

---

## 8. Public-facing relationship reflection and legal-process guide

Create a separate page titled **Relationship Reflection & Divorce Process Guide**.

This is a general information and reflection tool, not a diagnostic instrument.

### A. Optional questionnaire

Ask concise, plain-language questions such as:

- Is the user asking about relationship concerns or an existing legal case?
- Which concerns are relevant: communication, trust, recurring conflict, finances, family interference, incompatibility, or other?
- Have the concerns been discussed?
- Would discussing them together feel safe?
- Is the user interested in reconciliation information, separation information, or the legal process?
- Has a petition already been filed?
- If so, what general procedural stage is it at?
- Would the user like information about legal rights, counselling, mediation, or qualified support?

Allow skipping questions. Avoid names, contact details, exact addresses, case numbers, and unnecessary intimate narratives.

### B. Relationship reflection results

Return a structured, non-diagnostic summary of selected concerns, questions for reflection, general support options, and possible next steps.

Do not output a numerical probability that the marriage will end in divorce. Do not label people as likely-to-divorce spouses, diagnose anyone, infer a partner's intentions, or claim that particular answers predict divorce.

If the user indicates fear, coercion, threats, or abuse, prioritize safety-oriented information and suitable support. Never automatically recommend joint counselling or confrontation when doing so may be unsafe.

### C. Legal-process guide

Ask only broad, relevant questions, such as whether the query concerns mutual-consent or contested proceedings, whether a petition has been filed, and whether the user seeks information about filing, mediation/counselling, hearings, or disposal.

Use verified Indian legal sources and applicable legislation. Account for differences in applicable personal law and case circumstances rather than assuming one process fits everyone. Cite the relevant official source and version/date when available. Explain that the guide is general information, not individualized legal advice.

Do not predict that a particular petition will be granted or dismissed based on a questionnaire.

### D. Contextual historical statistics

If reliable court data exists, display cohort-level counts, observed disposition distributions, duration distributions, time period, sample size, coverage, and uncertainty.

Use language such as “Among the observed cases in this dataset…” Never turn a general historical rate into “your case has an X% chance” without evidence that the cohort and individual's case are genuinely comparable and that the estimate is validated.

### E. Privacy requirements

- Make questionnaire answers optional.
- Process responses in memory where practical.
- Do not persist answers by default.
- Do not send relationship details to third-party AI services.
- Do not use questionnaire answers to train models.
- Exclude sensitive answers from logs and analytics.
- Prevent cross-user access to responses.
- Do not collect information about a partner without their participation or consent.
- Display a clear privacy notice.
- Do not present the feature as therapy, legal representation, or an emergency service.

---

## 9. Aggregate court-workload forecasting

Keep workload forecasting separate from case-outcome prediction.

Forecast aggregate divorce-specific filings or pendency only if reliable historical data supports the task.

Compare appropriate baselines first:

- Naive forecast.
- Seasonal naive forecast where seasonality is supported.
- Poisson or negative-binomial regression when appropriate.
- SARIMA or another defensible time-series model.
- More complex ML only if observation volume justifies it.

Use chronological training/validation/testing and rolling-origin evaluation where feasible. Report MAE, RMSE, appropriate count-based metrics, prediction intervals, and baseline comparisons.

Do not forecast at district level if data does not support that granularity. Do not confuse an aggregate count forecast with a prediction about an individual's case.

---

## 10. Simple, interactive, fully functional GUI

For the first usable version, keep the GUI **simple, clean, responsive, and easy to navigate**. Prioritize functionality and clarity over visual effects, elaborate animation, or complex design systems.

Use a practical Python-first stack, preferably Streamlit with Plotly, pandas, NumPy, SciPy, statsmodels, and scikit-learn. Use SQLite for metadata if useful. Add a separate API or frontend framework only if there is a clear requirement.

### Required pages

1. **Overview** — project objectives, validated key findings, coverage, last successful refresh, source status, and limitations.
2. **Court Activity** — filings, disposals, pendency, trends, and comparable district/court breakdowns.
3. **Demographics** — divorced/separated population distributions, valid denominators, reference year, and demographic/geographic filters.
4. **Statistical Laboratory** — supported tests, assumptions, effect sizes, confidence intervals, p-values, and interpretation.
5. **Court Outcome Research** — outcome definitions, class balance, model evaluation, calibration, confusion matrices, and limitations.
6. **Workload Forecasting** — supported series, baselines, forecasts, uncertainty intervals, and evaluation.
7. **Relationship Reflection & Divorce Process Guide** — optional questionnaire, reflection, general legal information, official citations, and appropriate support resources.
8. **Data & Methodology** — source registry, data dictionary, quality report, coverage, refresh history, model cards, limitations, and permitted exports.

### GUI acceptance requirements

- Every filter changes the displayed results correctly.
- Every button performs its advertised action.
- Charts display actual processed data or verified model outputs.
- Empty or unavailable data produces a clear message, not a crash or fabricated chart.
- Missing values are never silently presented as zero.
- Labels identify source and reference period.
- Data downloads contain the data currently selected, where applicable.
- The app starts even when external data sources are unavailable.
- The app clearly distinguishes verified findings, exploratory analysis, predictions, and unavailable features.
- The layout works on ordinary desktop and mobile-sized viewports.
- Avoid unnecessary pages, excessive cards, decorative dashboards, and nonfunctional controls.

---

## 11. Suggested project structure

Inspect the workspace first, then adapt this structure as appropriate while preserving separation of concerns.

```text
tamil-nadu-divorce-analysis/
├── app.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
├── pyproject.toml
├── config/
│   ├── settings.yaml
│   └── source_registry.yaml
├── data/
│   ├── raw/
│   ├── interim/
│   ├── processed/
│   └── metadata/
├── src/
│   ├── ingestion/
│   ├── cleaning/
│   ├── validation/
│   ├── geography/
│   ├── statistics/
│   ├── models/
│   │   ├── workload_forecasting.py
│   │   ├── outcome_prediction.py
│   │   ├── survival_analysis.py
│   │   └── evaluation.py
│   ├── assessment/
│   │   ├── questionnaire.py
│   │   ├── relationship_reflection.py
│   │   └── legal_information.py
│   ├── reporting/
│   └── utils/
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── data_quality/
│   ├── model_validation/
│   ├── ui/
│   └── fixtures/
├── notebooks/
├── docs/
│   ├── architecture.md
│   ├── build_log.md
│   ├── directory_guide.md
│   ├── file_guide.md
│   ├── data_sources.md
│   ├── data_dictionary.md
│   ├── methodology.md
│   ├── model_cards.md
│   ├── limitations.md
│   ├── privacy.md
│   ├── testing.md
│   ├── decisions.md
│   └── final_report.md
└── outputs/
    ├── figures/
    ├── tables/
    └── reports/
```

Do not create empty placeholder modules merely to match this tree. Every committed module must have a defined purpose, meaningful implementation, or a documented reason for being deferred.

---

## 12. Mandatory documentation: every step, file, directory, model, and feature

**Documentation is a core deliverable, not an optional final task.** Maintain it continuously while building the project. Do not attempt to reconstruct the entire development history at the end.

### A. Build log — `docs/build_log.md`

Document the development process chronologically. For each meaningful step, record:

- Step ID and date/time.
- Objective.
- Why the step was needed.
- Files created, read, modified, or deleted.
- Directory changes.
- Implementation summary.
- Important decisions and alternatives considered.
- Commands or workflows executed.
- Tests run and their results.
- Errors encountered.
- Root cause analysis.
- Fix applied.
- Remaining issues.
- Next step.

Do not record secrets, tokens, credentials, personal data, or sensitive environment values.

### B. Directory guide — `docs/directory_guide.md`

Explain every project directory:

- Its responsibility.
- What belongs there.
- What must not be stored there.
- Dependencies on other directories.
- How data or code flows through it.

Update this file whenever the directory structure changes.

### C. File guide — `docs/file_guide.md`

Maintain a complete file-by-file inventory of project-owned files, excluding generated caches and irrelevant environment artifacts.

For each file, document:

- Relative path.
- Purpose.
- Why it exists.
- Key functions/classes/components.
- Inputs and outputs.
- Dependencies and callers.
- Configuration it reads.
- Data it reads or writes.
- Tests that cover it.
- Whether it is implemented, experimental, deferred, or deprecated.

Keep this inventory synchronized with the repository. Include notebooks, scripts, configuration, tests, UI files, documentation, and model artifacts that are intentionally tracked.

### D. Architecture — `docs/architecture.md`

Document:

- System architecture.
- Module boundaries.
- Data-flow diagrams.
- Ingestion-to-dashboard flow.
- Model-training and inference flow.
- User questionnaire flow.
- Source-of-truth definitions.
- Error-handling paths.
- Security and privacy boundaries.

Use Mermaid diagrams in Markdown where helpful.

### E. Model cards — `docs/model_cards.md`

Create a separate card for each model or model family, including:

- Intended use.
- Prohibited or inappropriate uses.
- Target definition.
- Training data source and coverage.
- Feature definitions and prediction time.
- Preprocessing.
- Baseline.
- Model selection process.
- Split strategy.
- Evaluation metrics.
- Held-out results.
- Calibration.
- Known biases.
- Limitations.
- Reproducibility instructions.
- Model version and artifact location.

Document failed experiments and explain why a model was rejected. Never report training performance as held-out performance.

### F. Data documentation

Maintain:

- `docs/data_sources.md`
- `docs/data_dictionary.md`
- Source registry.
- Data-quality report.
- Transformation and mapping rules.
- Raw-file checksums.
- Retrieval timestamps.
- Missingness and coverage reports.
- Provenance from each output back to its source.

For each processed dataset, explain the transformation steps and how to reproduce it.

### G. Decisions and limitations

Use `docs/decisions.md` to record important architectural, statistical, and product decisions with rationale and alternatives.

Use `docs/limitations.md` to document source gaps, sampling bias, missing labels, outdated reference periods, legal uncertainties, modelling constraints, and features not supported by evidence.

### H. Documentation accuracy

- Update documentation whenever code, data schemas, APIs, models, directory structure, or UI behavior changes.
- Do not claim that a feature works until its implementation and tests support that claim.
- Mark incomplete functionality clearly.
- Include actual commands, not vague instructions.
- Use relative links between documentation files.
- Verify that internal documentation links resolve.
- Never invent test results, source retrievals, model metrics, or completed steps.

---

## 13. Automated test suite and self-correcting iteration loop

**The agent must continuously test its own work, diagnose failures, fix them, and rerun relevant tests.** Do not stop at writing test files. Execute the tests and inspect their actual results.

Use pytest or another suitable framework. Include unit tests, integration tests, data-quality tests, model-validation tests, and GUI smoke tests.

### A. Unit tests

Test:

- Parsing and normalization of every supported file format.
- Date parsing and invalid-date handling.
- Nonnegative count validation.
- Missing values versus true zero values.
- Category mapping.
- District crosswalk behavior.
- Duplicate and conflicting-record detection.
- Statistical calculations against known test examples.
- Confidence intervals and effect-size calculations.
- Correct handling of zero denominators.
- Forecasting input validation.
- Outcome-label mapping.
- Calibration and evaluation metric calculations.
- Questionnaire branching and skipped answers.
- Privacy-preserving defaults.
- CSV exports and selected filters.

### B. Integration tests

Test the end-to-end paths:

1. Official/raw file or test fixture → parser → normalized data.
2. Normalized data → validation → quality report.
3. Clean data → statistical calculations → exported results.
4. Time series → train/test split → baseline → forecast evaluation.
5. Eligible case data → leakage checks → model training → held-out evaluation.
6. Questionnaire answers → reflection output.
7. Legal-process selections → correct general information and source references.
8. Processed data → dashboard filters → charts and tables.
9. Selected dashboard data → CSV export.
10. Application startup when a source is unavailable.

Use small synthetic fixtures for deterministic software tests only. Mark them clearly as test fixtures and never include them in research outputs.

### C. Model-specific safeguards

Add tests that verify:

- No future information appears in training features.
- Target columns and post-outcome fields are excluded from predictors.
- Train/test time periods do not overlap improperly.
- Related or repeated records cannot cause obvious split leakage.
- Baselines are computed correctly.
- Evaluation metrics match hand-calculated examples.
- Probabilities are finite, bounded between zero and one, and sum appropriately for multiclass outputs.
- Calibration metrics fail clearly when inputs are invalid.
- Unsupported outcome classes do not silently disappear.
- Forecast intervals and outputs have valid shapes.
- Pending cases are treated as censored in survival analysis when appropriate.

### D. GUI tests

At minimum, test that:

- The application starts.
- Each page loads.
- Filters can be changed.
- Empty datasets show a useful message.
- Charts and tables render when valid test data is supplied.
- Export controls work.
- The questionnaire accepts skipped optional answers.
- Results do not falsely display individual divorce probabilities.
- Missing external data does not crash the application.
- The privacy notice is visible before the questionnaire.

Use Streamlit's testing tools or suitable browser automation if available. If full browser automation is unavailable, create the strongest practical smoke tests and document the limitation.

### E. Static checks and environment

Run suitable tools, for example:

- Test suite.
- Python import/compile checks.
- Linting and formatting checks.
- Type checks where useful.
- Dependency/environment checks.
- Documentation link checks.
- Git diff/status inspection.
- Secret scanning or checks for accidental credentials.
- Application startup smoke test.

Use tools that are actually installed or install suitable development dependencies when permitted. Do not claim a check ran if it did not.

### F. Required iteration loop

Follow this loop continuously:

1. Select a small, verifiable implementation objective.
2. Inspect the relevant code and documentation.
3. Implement the change.
4. Add or update tests for expected behavior and edge cases.
5. Run targeted tests.
6. Inspect failures and actual outputs.
7. Identify the root cause rather than suppressing the error.
8. Fix the implementation or, if the test expectation is wrong, correct the test with a documented rationale.
9. Rerun targeted tests.
10. Run related regression tests.
11. Update documentation and the build log.
12. Continue to the next objective.

After integration, run the full test suite and application smoke tests. When a failure occurs, keep iterating until the expected behavior is achieved or a genuine external blocker is demonstrated and documented.

Do not:

- Delete failing tests to make the suite pass.
- Weaken assertions without justification.
- Catch all exceptions and silently continue.
- fabricate successful test output.
- hide failed checks.
- use synthetic research data to make the application look complete.
- stop after the first successful launch if other required tests have not run.

Use bounded, practical iteration. If a failure persists, investigate dependencies, assumptions, and reproducibility; document the unresolved blocker honestly rather than looping indefinitely.

### G. Acceptance criteria for each feature

A feature is complete only when all applicable conditions are met:

- Implementation exists.
- Inputs and outputs are defined.
- Valid-input behavior is tested.
- Invalid and missing-input behavior is tested.
- Edge cases are tested.
- Errors are handled visibly and appropriately.
- Documentation describes actual behavior.
- Integration with dependent modules is tested.
- No unsupported claims appear in the UI or report.

---

## 14. Research report generation

Automatically generate a final report containing:

1. Abstract.
2. Research questions and hypotheses.
3. Background and motivation.
4. Official-source review.
5. Data collection methodology.
6. Data dictionary and preprocessing.
7. Data-quality assessment.
8. Exploratory analysis.
9. Probability and statistical methods.
10. Machine-learning methodology.
11. Model evaluation.
12. Results and figures.
13. Limitations and biases.
14. Privacy and ethical considerations.
15. Conclusions.
16. Future research.
17. References with working source links.

Clearly separate observed findings, statistical associations, predictions, and interpretation. Do not claim causality from observational associations without a defensible identification strategy. Do not invent results for analyses that could not be performed.

Generate downloadable aggregate tables and figures when permitted. Include source, reference period, and transformation notes for every reported result.

---

## 15. Environment, reproducibility, and delivery

Provide:

- `README.md` with setup, configuration, data acquisition, tests, and launch instructions.
- `requirements.txt` and, where appropriate, `pyproject.toml` with reproducible dependencies.
- `.env.example` containing variable names only, never real credentials.
- `.gitignore` excluding secrets, local environments, caches, and restricted raw data as appropriate.
- A command or documented workflow to rebuild processed data from available raw files.
- A command to run analyses.
- A command to run tests.
- A command to launch the app.
- Clear guidance for obtaining any data that cannot legally or technically be bundled.
- A clear distinction between code artifacts, research outputs, raw source data, and synthetic test fixtures.

Prefer a simple local-first setup. Do not require paid services or external AI APIs for the core application unless genuinely necessary. The public-facing questionnaire should work without sending sensitive answers to an external service.

Before final delivery, verify the exact files and commands in the current workspace. Never invent a path or claim an artifact exists without checking.

---

## 16. Autonomous execution stages

Execute these stages in order, continuously updating the documentation and test suite.

### Stage 1 — Workspace audit

Inspect the repository, runtime, installed tools, current code, and available files. Preserve useful work. Establish a task checklist and document the initial state.

### Stage 2 — Source feasibility

Investigate official data sources and determine what is actually obtainable, permitted, and sufficiently granular. Save the source report.

### Stage 3 — Ingestion

Implement permitted data retrieval and manual-import fallbacks. Preserve raw data, checksums, timestamps, and provenance.

### Stage 4 — Data quality

Implement schemas, cleaning, district crosswalks, validation, deduplication logic, and quality reports. Add tests.

### Stage 5 — Statistics

Implement supported descriptive, inferential, regression, and survival analyses. Validate calculations against known test examples.

### Stage 6 — Predictive models

Build workload forecasting if supported. Build historical outcome prediction only when valid labels and sufficient data exist. Evaluate with leakage-resistant splits and documented metrics.

### Stage 7 — Public assessment

Build the privacy-preserving relationship reflection and legal-process guide. Keep it separate from the court-outcome research model.

### Stage 8 — GUI integration

Build the simple interactive dashboard and connect every displayed result to real processed data or verified model output.

### Stage 9 — Test-and-fix cycle

Run unit, integration, model-validation, GUI, and regression tests. Fix failures and rerun them. Do not proceed by hiding failures.

### Stage 10 — Documentation synchronization

Complete and verify the build log, directory guide, file guide, architecture, data documentation, model cards, decisions, limitations, testing guide, and final report. Update them continuously as implementation evolves.

### Stage 11 — Final validation

Start the application from the documented clean setup, verify critical user flows, run the full available test suite, inspect the repository for secrets and placeholder functionality, and verify that documentation matches actual behavior.

### Stage 12 — Final handoff

Report what is actually complete, what data was retrieved, what analyses ran, which models were trained and evaluated, the real test results, the launch command, and any remaining blockers.

---

## 17. Definition of done

The project is complete only when:

- The application launches with documented instructions.
- Official source availability and limitations are documented.
- All retrieved data has provenance and validation records.
- Statistical results are reproducible.
- Models have held-out evaluation rather than only training scores.
- Unsupported predictions are withheld.
- The relationship questionnaire does not claim to predict whether a marriage will end in divorce.
- Legal guidance cites verified sources and does not promise court outcomes.
- No fabricated observations, model metrics, or unsupported probabilities appear.
- The GUI is simple, interactive, responsive, and functionally connected to the data.
- Automated tests cover critical logic, data processing, models, privacy-sensitive behavior, and user flows.
- Tests have actually been executed; failures are fixed or explicitly documented as unresolved external blockers.
- The agent has maintained file-wise, directory-wise, model-wise, and feature-wise documentation throughout development.
- The build log records meaningful changes, commands, failures, fixes, and test results.
- Documentation matches the final codebase.
- Any incomplete feature is clearly labelled rather than represented as complete.

## 18. Final operating instructions

Prioritize scientific validity, privacy, reproducibility, and functional correctness over feature count or visual polish.

Do not substitute general court statistics for divorce-specific statistics. Do not invent an outcome classifier when outcome labels are inadequate. Do not show personalized divorce or court-approval probabilities unsupported by validated evidence. If only demographic data can be retrieved, deliver a valid demographic study and clearly document the missing judicial evidence.

Keep the first GUI simple and fully functional. Add complexity only when it serves a real research or user need.

Maintain documentation continuously. Test every meaningful implementation increment. Diagnose failures, fix root causes, and rerun tests until expected behavior is achieved or a genuine blocker is documented.

**Start now by inspecting the existing workspace and conducting the official-data feasibility audit. Then execute the full project autonomously. Do not stop at planning; build, test, document, and verify the actual application.**
