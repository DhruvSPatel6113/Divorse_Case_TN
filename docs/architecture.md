# System Architecture & Technical Specifications

This document outlines the architecture, data flows, module boundaries, and security/privacy guarantees of the Tamil Nadu Divorce and Matrimonial Judicial Analysis platform per Section 12.D.

---

### High-Level System Architecture

```mermaid
graph TD
    subgraph Data Tier
        RawCensus["Official Census 2011 XLS<br>(DDW-3300C-02-fer3-MDDS.xls)"]
        RawCourt["Official Court Returns<br>(Lok Sabha / DoJ / NJDG)"]
        RawCensus --> DemoClean["Demographic Cleaner<br>(SHA-256 Verified)"]
        RawCourt --> CourtClean["Court Cleaner<br>(Scope Enforcer)"]
        Crosswalk["District Crosswalk<br>(32 to 38 Districts)"] --> DemoClean
        Crosswalk --> CourtClean
        DemoClean --> CleanDemo["data/processed/demographic_tn_2011.parquet"]
        CourtClean --> CleanCourt["data/processed/court_aggregate_tn.parquet"]
    end

    subgraph Analytical Core
        CleanDemo --> StatLab["Statistical Lab<br>(Experiments 1 - 7)"]
        CleanCourt --> StatLab
        CleanCourt --> Forecast["Workload Forecaster<br>(ARIMA / Holt / Poisson)"]
        CleanCourt --> Outcome["Outcome Research Pipeline<br>(Leakage Audited)"]
    end

    subgraph User Assessment & Guidance
        User["Public Litigant / Citizen"] --> Quest["In-Memory Questionnaire<br>(Zero Persistence)"]
        Quest --> Reflect["Reflection Engine<br>(Safety Escrow)"]
        Quest --> Legal["Legal Information Guide<br>(HMA, SMA, PWDVA)"]
        Reflect -.->|"Emergency Alert (181 / 112)"| Safety["State Helplines & Legal Aid"]
    end

    subgraph GUI Presentation
        StatLab --> App["Interactive Streamlit Portal<br>(8 Verified Pages)"]
        Forecast --> App
        Outcome --> App
        Reflect --> App
        Legal --> App
    end
```

---

### Key Architectural Boundaries

1. **Separation of Measurement Scopes:**
   - **Demographic Stock:** Census population snapshot counts (`demographic_marital_status`).
   - **Matrimonial Broad:** Family Court proceedings under Family Courts Act, 1984 (`matrimonial_broad`).
   - **All Civil Cases:** Subordinate judiciary civil backlog from NJDG (`all_cases`).
   - These scopes are kept strictly isolated in data representations to prevent false equivalences.

2. **Feature Leakage Prevention in Outcome Research:**
   - Pre-filing features (marriage duration, statute, petitioner type, counsel representation) are verified by an automated blacklist auditor.
   - Any feature generated after petition presentation (`disposal_date`, `interim_maintenance_ordered`, `final_order_date`) is strictly blocked from the feature matrix.

3. **Privacy and In-Memory Execution:**
   - The Relationship Reflection tool collects no personally identifiable information (PII).
   - Questionnaire responses live solely within the user's active session state in RAM; no external API calls, third-party LLMs, or database persistence mechanisms are utilized.

4. **Safety-First Routing Protocol:**
   - Responses indicating physical violence, coercion, or severe fear bypass normal reflection synthesis and immediately trigger high-visibility emergency safety alerts featuring Tamil Nadu's 24/7 Women Helpline (181) and National Emergency Services (112).
