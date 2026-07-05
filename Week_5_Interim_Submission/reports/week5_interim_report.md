
# Week 5 Interim Report: Data Profiling and Schema Mapping

## Introduction

The Week 5 interim task focused on understanding the structure and clinical meaning of an emergency department triage dataset. The dataset contains 55,121 emergency department visits and 226 original columns. These include demographic variables, arrival-related variables, triage vital signs, glucose values, disposition-related information, and 200 chief complaint indicator columns.

The main target variable is `esi`, which represents the Emergency Severity Index triage level. This variable was treated as the outcome for analysis and future modelling.

## Target Variable Analysis

The ESI distribution showed that most visits were assigned ESI 3, representing 49.00% of the dataset. ESI 2 represented 32.52%, ESI 4 represented 16.14%, ESI 5 represented 2.20%, and ESI 1 represented only 0.14%.

This shows that the dataset is imbalanced. ESI 3 and ESI 2 dominate the dataset, while ESI 1 cases are rare. This is important for future modelling because a model may perform poorly on rare high-acuity cases if class imbalance is not considered.

## Schema Mapping

A schema mapping approach was used to separate the dataset into clinically meaningful groups. The dataset contained 200 chief complaint indicator columns, 9 demographic features, 8 triage clinical measurement variables, 5 arrival or operational variables, 2 potential leakage variables, 1 target variable, and 1 identifier/index column.

The columns `disposition` and `previousdispo` were identified as potential leakage variables. These should not be used as predictive model features because they may reflect patient outcomes or later clinical decisions rather than information available at the point of triage.

## Vital Sign Profiling

The triage vital sign variables included heart rate, systolic blood pressure, diastolic blood pressure, respiratory rate, oxygen saturation, oxygen device use, temperature, and glucose. These variables had no missing values in the dataset.

The median vital signs were fairly similar across ESI levels. Median heart rate was approximately 85 bpm, median systolic blood pressure was 132 mmHg, median diastolic blood pressure was 79 mmHg, median respiratory rate was 18 breaths per minute, median oxygen saturation was 98%, median temperature was approximately 98.0°F, and median glucose was 107 mg/dL.

Temperature was interpreted as Fahrenheit, which is important for correct clinical interpretation. Glucose showed a wide range from 16 to 1066, suggesting the presence of extreme values or severe clinical cases.

## Chief Complaint Cleaning

The dataset contained 200 chief complaint columns beginning with `cc_`. These columns were expected to represent complaint presence or absence. However, nine chief complaint columns contained values greater than 1. To standardise these variables, all chief complaint columns were converted to binary format, where 0 indicated the complaint was not present and 1 indicated the complaint was present.

After this cleaning step, the most common chief complaint was abdominal pain, present in 6,716 visits or 12.18% of the dataset. Other common complaints included other, chest pain, shortness of breath, back pain, fall, cough, dizziness, leg pain, emesis, weakness, and flank pain.

## Body-System Grouping

The 200 chief complaint columns were grouped into broader body-system families to improve clinical interpretability. The complaint families included musculoskeletal/trauma, gastrointestinal, respiratory, general/constitutional/other, neurologic, cardiovascular, mental health/substance/toxicology, skin/wound/infection, eye/ENT/oral, genitourinary, endocrine/metabolic, and other/needs review.

The most common complaint family was musculoskeletal/trauma, present in 12,182 visits or 22.10% of the dataset. This was followed by gastrointestinal complaints at 19.63%, respiratory complaints at 12.98%, general/constitutional/other complaints at 12.44%, neurologic complaints at 11.49%, and cardiovascular complaints at 9.72%.

## Complaint Families by ESI Level

The complaint-family analysis showed clinically meaningful variation across ESI levels. Neurologic complaints were highest in ESI 1 visits at 49.35%. Cardiovascular complaints were highest in ESI 2 visits at 18.09%. Gastrointestinal complaints were highest in ESI 3 visits at 31.29%. Musculoskeletal/trauma complaints were highest in ESI 4 visits at 51.28%. Skin/wound/infection complaints were highest in ESI 5 visits at 30.31%.

These patterns suggest that different complaint families may be associated with different levels of triage acuity. However, ESI 1 had only 77 cases, so findings for ESI 1 should be interpreted cautiously.

## Data Quality Issues

One data quality issue was identified in the `arrivalhour_bin` column. Some values appeared to have been affected by spreadsheet date formatting. The values `14-Nov`, `10-Jul`, and `6-Mar` were cleaned to `11-14`, `07-10`, and `03-06`, respectively.

Another data quality issue was the presence of non-binary values in some chief complaint columns. This was corrected by converting all chief complaint values greater than 0 to 1.

## Modelling Preparation

For future modelling, the recommended target variable is `esi`. The columns `original_index`, `disposition`, `previousdispo`, and the original `arrivalhour_bin` should be excluded from the modelling feature set. The cleaned `arrivalhour_bin_clean` column should be used instead of the original arrival hour column.

After cleaning and feature engineering, the final analysis dataset contained 55,121 rows and 239 columns. There were 234 safe feature columns after excluding the target, identifier, leakage-risk variables, and the original arrival-hour column.

## Conclusion

The Week 5 interim analysis successfully profiled the dataset, mapped variables into clinically meaningful groups, identified potential leakage variables, cleaned chief complaint indicators, corrected an arrival-hour formatting issue, and grouped chief complaints into interpretable body-system families. These steps provide a stronger foundation for future modelling and clinical interpretation of emergency department triage acuity.
