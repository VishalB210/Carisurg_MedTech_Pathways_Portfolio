# Week 6 Final Submission - Baseline Triage Models

**Student:** Vishal Baboolal  
**Random seed:** `42`

## Contents

- `notebooks/week6_final_baseline_models.ipynb` - executed modelling and evaluation notebook.
- `docs/week6_baseline_report.pdf` - final report, three pages or less.
- `docs/week6_baseline_report.md` - editable report.
- `docs/model_comparison_metrics.csv` - benchmark table for all three models.
- `docs/logistic_regression_classification_report.csv` - per-class results.
- `docs/decision_tree_classification_report.csv` - per-class results.
- `docs/dummy_baseline_classification_report.csv` - random-baseline results.
- `docs/figures/logistic_regression_confusion_matrix.png` - logistic-regression confusion matrix.
- `docs/figures/decision_tree_confusion_matrix.png` - decision-tree confusion matrix.
- `docs/figures/confusion_matrices_comparison.png` - report-ready comparison image.
- `docs/figures/model_comparison_chart.png` - metric comparison chart.
- `docs/one_minute_clinical_explainer_script.md` - clinician-friendly video script.
- `docs/loom_video_link.md` - placeholder for the recorded video link.

## Models

1. Stratified random baseline
2. Logistic regression
3. Decision tree with `max_depth=12`

All models use the same 80/20 stratified split and `random_state=42`.

## Main finding

Logistic regression was the strongest overall baseline at **66.7% accuracy**, but it correctly identified only **4 of 16 ESI Level 1 patients**. The decision tree identified only **1 of 16**. Neither model is suitable for clinical deployment.

## Primary metric

ESI Level 1 recall is the primary clinical safety metric because missing a truly critical patient can delay immediate life-saving care.

## Data governance

The patient-level dataset is not included. The notebook searches for `data_cleaned_week5.csv` locally or in Google Drive. Do not commit the raw or cleaned patient-level CSV to a public repository.

## Remaining manual action

Record the one-minute clinical explainer, post it to Discord, and paste its link into `docs/loom_video_link.md`.
