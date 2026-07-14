# Week 6 Baseline Model Report

**Student:** Vishal Baboolal  
**Programme:** CariSurg MedTech Pathways Programme 2026  
**Project:** AI-Assisted Emergency Department Triage  
**Random seed:** `42`

## One-sentence verdict

The dataset contains enough signal to outperform stratified random guessing, but neither baseline is safe for clinical deployment because both miss most ESI Level 1 patients.

## 1. Dataset recap

The cleaned Week 5 dataset contains **55,121 emergency department encounters** and **225 columns**. The target is Emergency Severity Index (`esi`), where Level 1 is the most urgent and Level 5 is the least urgent. The model used **208 numeric clinical features** available before or during triage. Post-triage leakage variables (`disposition` and `previousdispo`), administrative variables, and fairness-sensitive demographic variables were excluded. An **80/20 stratified split** produced **44,096 training records** and **11,025 test records**.

## 2. Models

- **Stratified random baseline:** predicts classes according to the training class distribution.
- **Logistic regression:** a scaled linear multi-class baseline that estimates class boundaries from all selected features.
- **Decision tree:** a non-linear rule-based baseline with `max_depth=12`. The depth cap was used to limit overfitting while still allowing enough branches to represent five ESI levels.

## 3. Benchmark table

| Model | Accuracy | Macro F1 | Weighted F1 | ESI 1 recall | ESI 2 recall |
|---|---:|---:|---:|---:|---:|
| Stratified random | 0.375 | 0.204 | 0.375 | 0.000 | 0.327 |
| Logistic regression | 0.667 | 0.492 | 0.661 | 0.250 | 0.608 |
| Decision tree | 0.585 | 0.303 | 0.535 | 0.062 | 0.410 |

Logistic regression was the strongest overall baseline. It achieved **66.7% accuracy**, compared with **37.5%** for random guessing and **58.5%** for the decision tree.

## 4. Primary metric and clinical justification

The primary metric is **ESI Level 1 recall**: the proportion of truly Level 1 patients correctly identified. Overall accuracy is unsafe as the main measure because only 77 of 55,121 encounters are ESI 1. A model could appear accurate while overlooking critically ill patients. Missing an ESI 1 patient can delay immediate resuscitation, airway support, haemodynamic stabilisation, or other life-saving care.

Logistic regression identified **4 of 16** Level 1 patients (**25.0%**). The decision tree identified **1 of 16** (**6.2%**). Neither result is clinically acceptable.

## 5. Macro versus weighted F1

Macro F1 gives every ESI class equal importance, so poor performance on rare classes strongly lowers the score. Weighted F1 gives more influence to common classes, especially ESI 2 and ESI 3. The gap between logistic regression's macro F1 (**0.492**) and weighted F1 (**0.661**) shows that the model performs much better on common classes than on rare ESI 1 and ESI 5 cases.

## 6. Failure modes

The most serious failure is **under-triage of ESI Level 1 patients**. Logistic regression missed **12 of 16** critical cases. The decision tree missed **15 of 16**. The tree also concentrated predictions in the common middle classes and failed to identify ESI 5 in the held-out set. These errors reflect severe class imbalance and the limited number of ESI 1 examples available for learning.

The patients most at risk are critically ill people whose presentation is subtle or whose vital signs initially appear near normal. Their chief complaint or clinical context may carry urgency that a simple baseline does not capture adequately.

## 7. Recommendation and next steps

Proceed only as an offline research exercise. Do not deploy either baseline. The next stage should:

1. test class weighting or carefully designed resampling;
2. tune models using cross-validation without touching the held-out test set;
3. examine ESI 1 and ESI 2 errors case-by-case using de-identified summaries;
4. evaluate subgroup performance across age, sex, race, ethnicity, language, insurance status, and arrival mode;
5. assess calibration and alert burden;
6. validate on local Caribbean emergency department data before any silent pilot.

## Reproducibility and governance

All models use `random_state=42` and the same stratified split. The raw patient-level CSV is excluded from the public repository. Only aggregate metrics, classification reports, plots, and the executed notebook are committed.
