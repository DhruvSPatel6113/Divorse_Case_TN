# Statistical & Machine Learning Methodology

This document details the scientific methodology, analytical formulations, and evaluation protocols implemented in the research platform per Section 6, 7, and 9.

---

### 1. Demographic Inference & Disparity Metrics
- **Wilson Score Interval for Proportions:** Binomial confidence intervals are calculated using the Wilson score interval formula, which outperforms normal approximation intervals especially near boundary values:
  $$\tilde{p} = \frac{p + \frac{z^2}{2n}}{1 + \frac{z^2}{n}} \pm \frac{z}{1 + \frac{z^2}{n}} \sqrt{\frac{p(1-p)}{n} + \frac{z^2}{4n^2}}$$
- **Sex Disparity Odds Ratio:**
  $$\text{OR} = \frac{\text{Divorced Females} / \text{Married Females}}{\text{Divorced Males} / \text{Married Males}}$$
- **Contingency Testing:** Tested via Pearson's Chi-Square Test of Independence with Yates' continuity correction and Cramer's V effect size.

---

### 2. Time Series & Workload Forecasting
- **Candidate Models:**
  1. *Naive Persistence Baseline:* $\hat{y}_{t+h} = y_t$
  2. *Moving Average Baseline:* $\hat{y}_{t+h} = \frac{1}{k}\sum_{i=0}^{k-1} y_{t-i}$ (Window $k=2$)
  3. *Holt's Linear Exponential Smoothing:*
     $$\ell_t = \alpha y_t + (1-\alpha)(\ell_{t-1} + b_{t-1}), \quad b_t = \beta(\ell_t - \ell_{t-1}) + (1-\beta)b_{t-1}$$
  4. *Poisson Count GLM:*
     $$\log(\mathbb{E}[Y_t]) = \beta_0 + \beta_1 t + \beta_2 \text{Courts}_t$$
  5. *ARIMA(1, 1, 0) Process:*
     $$(1 - \phi_1 B)(1 - B) Y_t = \epsilon_t$$
- **Split Strategy:** Strict chronological training on earlier years (2018–2022) with holdout evaluation on subsequent years (2023–2024).
- **Evaluation:** Evaluated by MAE, RMSE, and MAPE. Prediction intervals generated via empirical standard error expansion ($z_{0.80} \approx 1.28$, $z_{0.95} \approx 1.96$).

---

### 3. Case Duration & Survival Analysis
- **Censoring Formulation:** All active pending cases in the court system are treated as formally right-censored at the snapshot observation cutoff.
- **Empirical Survival Function:**
  $$S(t) = P(T > t) = 1 - \sum_{k \le t} P(\text{Bracket}_k)$$
  Where $t \in \{0, 1, 3, 5, 10\}$ years. Evaluates the probability that a case remains active beyond $t$ years.

---

### 4. Feature Leakage Prevention Protocol
- **Temporal Epoch Enforcement:** All predictive features must represent facts knowable at or before the petition filing timestamp.
- **Automated Blacklist Filtering:** Scans candidate feature matrices to detect and drop any variables derived post-filing (`disposal_date`, `interim_maintenance_ordered`, `final_order_date`).
- **Ethical Restriction:** Individual court outcome probability predictions are withheld from public deployment to prevent unwarranted or misleading claims about judicial proceedings.
