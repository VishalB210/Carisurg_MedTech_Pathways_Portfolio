# Week 7 Interim Submission - Model Optimisation and Trade-offs

**Student:** Vishal Baboolal  
**Selected complex model:** Random Forest

## Submission contents

- `notebooks/week7_interim_random_forest_benchmark.ipynb`  
  Executed notebook containing the Week 6 baselines, the Week 7 random forest and the initial benchmark.

- `docs/week7_draft_benchmark_table.md`  
  GitHub-readable draft benchmark table and initial interpretation.

- `docs/week7_draft_benchmark_table.csv`  
  Machine-readable benchmark results.

- `docs/week7_interim_summary.md`  
  Short explanation of the model choice and initial trade-off.

- `docs/random_forest_classification_report.csv`  
  Per-class precision, recall and F1 values.

- `docs/random_forest_feature_importance.csv`  
  Complete random-forest feature-importance values.

- `docs/figures/random_forest_confusion_matrix.png`  
  Confusion matrix for the complex model.

- `docs/figures/random_forest_feature_importance.png`  
  Top 15 global feature importances.

## Reproducibility

The notebook reuses the Week 6 80/20 stratified split with `random_state=42`. The raw patient-level CSV is not included in the public submission.

## Interim status

This is an initial benchmark, not the final model recommendation. Hyperparameter tuning, deeper error analysis, the three-page cost-benefit memo and decision journal are reserved for the Week 7 final submission.
