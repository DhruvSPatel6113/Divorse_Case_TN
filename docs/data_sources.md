# Official Data Sources & Feasibility Audit

This document records the official data sources investigated, retrieved, and audited for the Tamil Nadu Divorce and Matrimonial Judicial Analysis project per Section 3 and Section 12.F.

---

### Source 1: Census of India 2011 — Table C-02 (Marital Status by Age and Sex)
- **Publisher:** Office of the Registrar General & Census Commissioner, India (ORGI), Ministry of Home Affairs.
- **Catalog Reference ID:** `PC11_C02-33`
- **Official URL:** [https://censusindia.gov.in](https://censusindia.gov.in)
- **Exact Download Endpoint:** [https://censusindia.gov.in/nada/index.php/catalog/10334/download/13446/DDW-3300C-02-fer3-MDDS.xls](https://censusindia.gov.in/nada/index.php/catalog/10334/download/13446/DDW-3300C-02-fer3-MDDS.xls)
- **Status:** **Verified & Successfully Retrieved** (537,600 bytes).
- **Raw Checksum (SHA-256):** `77f3bd417870b95d51320d818058dfa7c8129fc89197aec42d2d972fb450da74`
- **Retrieval Timestamp:** 2026-10-28T18:06:56Z
- **Coverage:** Tamil Nadu state total and all 32 districts (as of 2011), broken down by Residence (Total/Rural/Urban), 20 age groups, Sex (Persons/Males/Females), and 6 marital status categories.
- **Reconciliation Audit:** 0 discrepancies across 1,980 rows. State totals: Total Pop = 72,147,030; Divorced = 62,948; Separated = 398,284; Currently Married = 37,415,737.

---

### Source 2: Department of Justice — Family Courts & Cases Dashboard
- **Publisher:** Department of Justice, Ministry of Law & Justice, Government of India.
- **Official URL:** [https://doj.gov.in](https://doj.gov.in)
- **Dashboard Endpoint:** [https://dashboard.doj.gov.in/family-court-cases/](https://dashboard.doj.gov.in/family-court-cases/)
- **Status:** **Verified & Successfully Retrieved**.
- **Retrieval Timestamp:** 2026-10-28T18:06:30Z
- **Coverage:** State of Tamil Nadu (40 Functional Family Courts).
- **Verified Indicators:** 40 functional family courts; 2,396 monthly disposals; 31,655 active pending cases.
- **Scope:** Matrimonial Broad (Family Courts Act, 1984).

---

### Source 3: Parliament of India (Lok Sabha) — Ministry of Law & Justice Official Returns
- **Publisher:** Ministry of Law & Justice, Tabled in Lok Sabha / Digital Sansad.
- **Official URL:** [https://sansad.in](https://sansad.in)
- **Resource Reference:** Lok Sabha Unstarred Question No. 1134 (and related judicial pendency returns).
- **Status:** **Verified & Successfully Retrieved**.
- **Retrieval Timestamp:** 2026-10-28T18:05:00Z
- **Coverage:** Multi-year annual time series (2018–2024) for Tamil Nadu Family Courts.
- **Variables:** Annual cases filed (instituted), cases disposed, cases pending at year-end, and functional family court count.

---

### Source 4: National Judicial Data Grid (NJDG) — Subordinate Judiciary
- **Publisher:** e-Committee, Supreme Court of India / National Informatics Centre (NIC).
- **Official URL:** [https://njdg.ecourts.gov.in](https://njdg.ecourts.gov.in)
- **Status:** **Verified & Successfully Retrieved**.
- **Coverage:** 32 Judicial Districts of Tamil Nadu.
- **Variables:** District civil caseloads and duration brackets (<1 year, 1–3 years, 3–5 years, 5–10 years, >10 years).
- **Scope:** All Civil Cases / Subordinate judiciary workload profile.

---

### Source 5: eCourts Services — Individual Case-Level Microdata
- **Publisher:** eCourts Services / High Court of Madras.
- **Official Portal:** [https://services.ecourts.gov.in/ecourtindia_v6/](https://services.ecourts.gov.in/ecourtindia_v6/)
- **Status:** **Inaccessible for Automated Scraping (Bot Protection / CAPTCHA Terms)**.
- **Audit Findings:** Automated harvesting of eCourts case dockets is explicitly restricted by terms of use and protected by CAPTCHAs.
- **Compliance Policy:** In strict compliance with Section 3, Section 7, and Section 18, automated bypass was NOT performed. Individualized predictive modeling on live cases is withheld, while the research evaluation pipeline is benchmarked with deterministic research fixtures.
