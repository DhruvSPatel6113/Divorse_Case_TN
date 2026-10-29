# Architectural & Statistical Decision Record (ADR)

This document records the architectural, statistical, and product governance decisions made during the autonomous build, along with their rationale and considered alternatives, per Section 12.G.

---

### Decision 001: Strict Category Scope Differentiation
- **Context:** Judicial datasets often combine divorce petitions with child custody, restitution of conjugal rights, and maintenance under broader "Family Court" or "Civil" statistics.
- **Decision:** Enforce mandatory `category_scope` metadata tagging on every record:
  - `demographic_marital_status`: Census snapshot stock.
  - `matrimonial_broad`: Family Court proceedings under Family Courts Act, 1984.
  - `all_cases`: General civil court pendency from NJDG.
- **Alternatives Considered:** Labeling all Family Court cases as "Divorce cases". Rejected because doing so violates scientific honesty and statutory definitions.

---

### Decision 002: Withholding Individual Court-Outcome Predictions
- **Context:** Automated scrapers for eCourts case dockets are blocked by CAPTCHAs and terms of service. Deploying an unvalidated individual prediction model on synthetic data would deceive citizens about their legal rights.
- **Decision:** Implement the complete research evaluation pipeline with leakage checks and candidate classifiers, but **strictly withhold individualized probability predictions** from public deployment.
- **Alternatives Considered:** Training a classifier on synthetic data and presenting it as a working divorce predictor. Rejected per Section 1, 7, and 18 of the specification.

---

### Decision 003: Safety Escalation Protocol in Relationship Reflection
- **Context:** Users experiencing relationship distress may be in abusive or coercive situations where joint counselling or negotiation increases physical risk.
- **Decision:** Build an automated safety detection rule. If fear, domestic violence, or coercion is flagged, the system immediately suspends joint reflection advice and displays prominent emergency helplines (181, 112, TNSLSA).
- **Alternatives Considered:** Providing generic marital advice regardless of domestic violence indicators. Rejected as unethical and dangerous.

---

### Decision 004: In-Memory Only Questionnaire Processing
- **Context:** Litigants and individuals exploring marital dissolution have heightened privacy requirements.
- **Decision:** Process all questionnaire inputs in volatile session memory without disk or database persistence.
- **Alternatives Considered:** Storing responses in a local SQLite database or remote server. Rejected to eliminate cross-user data leakage and ensure zero persistent footprint.

---

### Decision 005: Local Storage for Project Chat History (User Rule 1)
- **Context:** User Global Rule 1 requires that project chat history be stored locally project-wise and kept out of remote repositories.
- **Decision:** Store chat logs in `chat_history/` and permanently ignore `.chat_history/` and `chat_history/` in `.gitignore`.
- **Alternatives Considered:** Storing chat logs in generic tmp folders or tracking them in git. Rejected per user instructions.
