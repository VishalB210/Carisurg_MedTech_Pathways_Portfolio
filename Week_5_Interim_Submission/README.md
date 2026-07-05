
# CariSurg Week 5 Interim Submission

## Project Overview

This Week 5 interim submission focuses on exploratory data profiling, schema mapping, chief complaint grouping, and preparation of an emergency department triage dataset for later modelling.

The dataset contains emergency department visit records with demographic information, arrival details, triage vital signs, glucose values, disposition-related columns, and chief complaint indicators.

## Dataset Summary

- Number of records: 55,121
- Original number of columns: 226
- Final cleaned analysis dataset columns: 239
- Target variable: `esi`
- Number of chief complaint columns: 200
- Number of body-system family columns created: 12

## Target Variable

The target variable is `esi`, which represents the Emergency Severity Index triage level.

ESI distribution:

| ESI Level | Count | Percent |
|---|---:|---:|
| 1 | 77 | 0.14% |
| 2 | 17,924 | 32.52% |
| 3 | 27,010 | 49.00% |
| 4 | 8,896 | 16.14% |
| 5 | 1,214 | 2.20% |

Most visits were ESI 3, followed by ESI 2 and ESI 4. ESI 1 cases were rare, representing only 0.14% of the dataset.

## Schema Mapping

The variables were grouped into the following roles:

| Variable Role | Number of Columns |
|---|---:|
| Chief complaint indicator | 200 |
| Demographic feature | 9 |
| Triage clinical measurement | 8 |
| Arrival / operational feature | 5 |
| Potential leakage variable | 2 |
| Target variable | 1 |
| Identifier / index | 1 |

The columns `disposition` and `previousdispo` were identified as potential leakage variables and were excluded from the recommended modelling feature set.

## Data Quality Notes

The `arrivalhour_bin` column contained values that appeared to be affected by spreadsheet formatting:

- `14-Nov` was corrected to `11-14`
- `10-Jul` was corrected to `07-10`
- `6-Mar` was corrected to `03-06`

Nine chief complaint columns contained values greater than 1. Since these columns represent complaint presence, all `cc_` columns were converted to binary format:

- 0 = complaint not present
- 1 = complaint present

## Vital Sign Summary

The dataset had no missing values for the triage vital sign variables.

Key vital sign observations:

- Median heart rate: 85 bpm
- Median systolic blood pressure: 132 mmHg
- Median diastolic blood pressure: 79 mmHg
- Median respiratory rate: 18 breaths/min
- Median oxygen saturation: 98%
- Median temperature: 98.0°F
- Median glucose: 107 mg/dL

Temperature was interpreted as Fahrenheit.

## Chief Complaint Findings

The most common chief complaint was abdominal pain, appearing in 6,716 visits or 12.18% of the dataset.

Top chief complaints included:

| Chief Complaint | Count | Percent |
|---|---:|---:|
| Abdominal pain | 6,716 | 12.18% |
| Other | 4,413 | 8.01% |
| Chest pain | 3,711 | 6.73% |
| Shortness of breath | 3,098 | 5.62% |
| Back pain | 1,997 | 3.62% |
| Fall | 1,924 | 3.49% |

## Body-System Complaint Families

The 200 chief complaint columns were grouped into broader body-system families to improve interpretability.

The most common complaint families were:

| Complaint Family | Count | Percent |
|---|---:|---:|
| Musculoskeletal / trauma | 12,182 | 22.10% |
| Gastrointestinal | 10,820 | 19.63% |
| Respiratory | 7,154 | 12.98% |
| General / constitutional / other | 6,856 | 12.44% |
| Neurologic | 6,331 | 11.49% |
| Cardiovascular | 5,359 | 9.72% |

## Complaint Families by ESI Level

Several clinically meaningful patterns were observed:

- Neurologic complaints were highest among ESI 1 visits at 49.35%.
- Cardiovascular complaints were highest among ESI 2 visits at 18.09%.
- Gastrointestinal complaints were highest among ESI 3 visits at 31.29%.
- Musculoskeletal / trauma complaints were highest among ESI 4 visits at 51.28%.
- Skin / wound / infection complaints were highest among ESI 5 visits at 30.31%.

ESI 1 only had 77 cases, so percentages for ESI 1 should be interpreted carefully.

## Files Included

- `week5_cleaned_analysis_dataset.csv`
- `schema_mapping.csv`
- `esi_distribution.csv`
- `vital_sign_summary.csv`
- `vital_signs_by_esi.csv`
- `chief_complaint_prevalence_clean.csv`
- `chief_complaint_family_mapping.csv`
- `complaint_family_prevalence_clean.csv`
- `complaint_family_by_esi_clean.csv`
- `esi_distribution.png`
- `top_20_chief_complaints_clean.png`
- `complaint_family_prevalence_clean.png`
- `complaint_family_by_esi_heatmap_clean.png`

## Summary

This Week 5 interim work prepared the dataset for future modelling by identifying the target variable, mapping columns into clinically meaningful roles, detecting potential leakage variables, cleaning chief complaint indicators, correcting an arrival-hour formatting issue, and grouping chief complaints into body-system families.
