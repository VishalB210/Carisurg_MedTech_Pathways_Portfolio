# Week 5 Feasibility Memo: AI-Assisted Triage Data Exploration

**To:** Dr. De Fretias and ED Board  
**From:** Vishal Baboolal  
**Project:** AI-assisted emergency department triage risk flagging  
**Dataset:** `yaleemmlc_admissionprediction_triage.csv`  
**Date:** Week 5 Final Submission

## One-sentence verdict

**Proceed with caveats:** this dataset is suitable for building a baseline triage model because it has 55,121 adult ED records, complete ESI labels, vital signs and 200 chief-complaint flags, but it should only be used after leakage removal, outlier review, fairness checks and external/local validation.

## Dataset summary

The dataset contains **55,121 patient records** and **226 raw columns**. After removing the original index column (`Unnamed: 0`), the cleaned working file contains **225 columns**. The target variable is **ESI**, where 1 is most urgent and 5 is least urgent. The dataset includes demographics, arrival details, vital signs, oxygen-device status, glucose, disposition variables and extensive one-hot encoded chief complaints.

Key profile:
- Age range: **18-107 years**, median **55**, mean **55.3**.
- Gender: **57.6% female**, **42.4% male**.
- Race: **53.4% White or Caucasian**, **29.0% Black or African American**, with smaller race categories under-represented.
- Ethnicity: **81.9% Non-Hispanic**, **17.9% Hispanic or Latino**.
- Arrival mode: **41.4% car**, **33.7% ambulance**.
- Chief complaints: 200 binary `cc_` flags; the most common is **abdominal pain (12.2%)**.
- Missing values: **0 missing values** were detected across the supplied file.
- Duplicate rows: **0 duplicates** after ignoring the original index column.

## Top 3 data-quality concerns

### 1. Leakage risk from post-triage variables

The dataset includes `disposition` and `previousdispo`. `disposition` occurs after ED assessment and treatment, so it must not be used as an input to a triage model. If a model learns from outcome variables that are only known after the triage decision, it will look artificially strong during testing and fail in real-time use.

**Action:** exclude `disposition`, `previousdispo`, and any other post-triage variables from model training unless their timestamp proves availability at triage.

### 2. Target imbalance

The target is clinically imbalanced. ESI 3 represents **49.0%** of records, ESI 2 represents **32.5%**, while ESI 1 is only **0.14%** and ESI 5 is **2.2%**. A model may appear accurate by performing well on common classes while failing to identify the rare but highest-acuity ESI 1 patients.

**Action:** evaluate with class-specific recall, confusion matrix, macro-F1 and high-acuity recall, not accuracy alone.

### 3. Extreme vital-sign values and transferability concerns

The vital-sign columns are complete, but some extreme values require clinical review. Examples include heart rate up to 221 bpm, systolic BP up to 266 mmHg, diastolic BP up to 189 mmHg, respiratory rate up to 66/min, temperature up to 106°F and glucose up to 1066 mg/dL. Some may be true critical values while others may be entry errors. The dataset also appears adult-only, single-context and based on US-style fields such as insurance status and arrival mode.

**Action:** keep clinically possible extremes, flag implausible values for review, and validate performance before transferring to a Caribbean public hospital setting.

## Top 3 reasons to proceed

### 1. Large sample size and complete target labels

The dataset has **55,121 records** with complete ESI labels. This is large enough for exploratory analysis and a baseline model, provided evaluation focuses on high-risk cases and class imbalance.

### 2. Clinically meaningful feature groups

The data includes variables that triage nurses use in real practice: age, arrival mode, vital signs, oxygen-device status, glucose and chief complaints. These features map directly to clinical triage reasoning.

### 3. Rich chief-complaint coverage

The 200 one-hot encoded chief-complaint flags provide strong clinical context. Common complaints such as abdominal pain, chest pain, shortness of breath, altered mental status and suicidal ideation are directly relevant to triage urgency.

## Top-10 feature shortlist

| Rank | Feature | Simple association with ESI | Clinical reasoning |
|---:|---|---:|---|
| 1 | `triage_vital_o2_device` | -0.219 | Patients needing supplemental oxygen are more likely to require urgent review; it has one of the strongest associations with lower ESI acuity level. |
| 2 | `triage_vital_o2` | 0.159 | Low oxygen saturation directly signals hypoxia and respiratory compromise, which should influence triage urgency. |
| 3 | `age` | -0.238 | Older adults have higher risk of deterioration and admission; age shows the strongest demographic association with ESI. |
| 4 | `cc_chestpain` | -0.164 | Chest pain may represent acute coronary syndrome and is one of the most common high-acuity complaints. |
| 5 | `cc_shortnessofbreath` | -0.15 | Shortness of breath can indicate respiratory failure, heart failure, asthma/COPD exacerbation or sepsis. |
| 6 | `triage_vital_hr` | -0.073 | Tachycardia or bradycardia can indicate shock, arrhythmia, pain, fever or physiological stress. |
| 7 | `triage_glucose` | -0.111 | Abnormal glucose can indicate diabetic emergencies or severe metabolic illness. |
| 8 | `cc_alteredmentalstatus` | -0.132 | Altered mental status is clinically high risk and associated with urgent neurologic, toxicologic, septic or metabolic causes. |
| 9 | `triage_vital_rr` | -0.056 | Respiratory rate is an early marker of deterioration and respiratory/metabolic stress. |
| 10 | `cc_suicidal` | -0.143 | Suicidal ideation is a safety-critical presentation requiring urgent mental health risk assessment. |

*Note: Lower ESI means higher urgency. Negative correlations indicate association with more urgent triage levels.*

## Caveats for the ED Board

This dataset is good enough for **baseline modelling and feasibility testing**, but not for direct clinical deployment. The first model should be used for offline evaluation only. Before any clinical use, the team should confirm timestamps, exclude leakage variables, test subgroup performance, review extreme values, monitor alert burden, and externally validate at the intended deployment site.

The safest next step is a Week 6 baseline model trained without leakage variables, evaluated using class-specific performance and accompanied by fairness checks across age, race, ethnicity, sex, language, insurance and arrival mode.
