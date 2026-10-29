# Data Dictionary & Schema Documentation

This document describes all variables, data types, constraints, and valid ranges across the processed datasets per Section 4 and Section 12.F.

---

### 1. Demographic Dataset (`data/processed/demographic_tn_2011.parquet` / `.csv`)

| Column Name | Data Type | Constraints / Allowed Values | Description |
| :--- | :--- | :--- | :--- |
| `source_id` | String | Fixed: `SRC_CENSUS_2011_C02` | Unique source identifier |
| `reference_year` | Integer | Fixed: `2011` | Census enumeration reference year |
| `district_original` | String | Non-empty | Original district string from raw census table |
| `district_code` | Integer | `0` to `32` (`0` = State Total) | 2011 Census of India numeric district code |
| `district_standardized` | String | Canonical district name | Standardized name mapped via `DistrictCrosswalk` |
| `residence_type` | String | `Total`, `Rural`, `Urban` | Residence sector grouping |
| `age_group` | String | `All ages`, `0-9`, `10-14`, ..., `80+`, `Age not stated` | Standard age brackets or summary categories |
| `is_summary_age_group` | Boolean | `True` / `False` | Flags aggregate categories (`All ages`, `Less than 18`, `Less than 21`) |
| `total_population_persons`| Integer | >= 0 | Total enumerated population (both sexes) |
| `total_population_males` | Integer | >= 0 | Enumerated male population |
| `total_population_females`| Integer | >= 0 | Enumerated female population |
| `never_married_persons` | Integer | >= 0 | Persons never married |
| `currently_married_persons`| Integer| >= 0 | Persons currently married |
| `widowed_persons` | Integer | >= 0 | Persons widowed |
| `separated_persons` | Integer | >= 0 | Persons legally or informally separated |
| `divorced_persons` | Integer | >= 0 | Persons legally divorced at census date |
| `divorced_separated_persons`| Integer| >= 0 | Combined marital disruption stock (`separated` + `divorced`) |
| `source_file` | String | `DDW-3300C-02-fer3-MDDS.xls` | Source file name |
| `retrieved_at` | String | ISO 8601 Timestamp | Raw file download timestamp |

---

### 2. Court Annual Time Series (`data/processed/court_time_series_tn.csv`)

| Column Name | Data Type | Constraints / Allowed Values | Description |
| :--- | :--- | :--- | :--- |
| `source_id` | String | `SRC_LOK_SABHA_FAMILY_COURTS` / `SRC_DOJ_FAMILY_COURTS_DASHBOARD` | Source identifier |
| `source_record_id` | String | Format: `TN_FC_{year}` | Unique record identifier |
| `state` | String | Fixed: `Tamil Nadu` | State jurisdiction |
| `district_standardized`| String | Fixed: `Tamil Nadu (State Total)` | Aggregate level |
| `category_scope` | String | Fixed: `matrimonial_broad` | Scope tag under Family Courts Act, 1984 |
| `period_start` | String | YYYY-MM-DD | Start of observation calendar year |
| `period_end` | String | YYYY-MM-DD | End of observation calendar year |
| `functional_courts` | Integer | >= 30 | Number of operating Family Courts in state |
| `cases_filed` | Integer | >= 0 | Nonnegative count of new cases instituted |
| `cases_disposed` | Integer | >= 0 | Nonnegative count of cases disposed/resolved |
| `cases_pending` | Integer | >= 0 | Nonnegative count of active unadjudicated matters |
| `clearance_rate_pct` | Float | >= 0.0 | Annual disposal clearance rate: `(disposed / filed) * 100` |
| `citation` | String | Official publication reference | Official parliamentary question or dashboard report citation |

---

### 3. District Judiciary Pendency Duration Dataset (`data/processed/court_districts_pendency_tn.csv`)

| Column Name | Data Type | Constraints / Allowed Values | Description |
| :--- | :--- | :--- | :--- |
| `source_id` | String | Fixed: `SRC_NJDG_TN_CIVIL` | Source identifier |
| `district_standardized`| String | Canonical 32 district names | District court complex location |
| `category_scope` | String | `all_cases` or `matrimonial_broad` | Scope distinction (overall civil vs family court) |
| `pendency_age_group` | String | `< 1 Year`, `1-3 Years`, `3-5 Years`, `5-10 Years`, `> 10 Years` | Duration bracket |
| `cases_pending` | Integer | >= 0 | Active cases within specific pendency cohort |
| `total_district_pending`| Integer | >= 0 | Total pending cases across all durations in district |
