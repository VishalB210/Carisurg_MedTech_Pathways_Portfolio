# Week 7 Final Submission - Model Optimisation and Trade-offs

**Student:** Vishal Baboolal  
**Project:** AI-Assisted Emergency Department Triage  
**Recommendation:** Advance optimised LightGBM to a silent Phase 3 pilot, with logistic regression retained as the transparent reference.

## Contents

- `notebooks/week7_final_model_optimisation.ipynb` - executed model screening, tuning and final benchmarking notebook.
- `docs/week-7-cost-benefit.pdf` - three-page board and IT governance memo.
- `docs/week-7-cost-benefit.md` - editable Markdown memo.
- `docs/week7_final_benchmark_table.md` - GitHub-readable comparison table.
- `docs/week7_final_benchmark_table.csv` - machine-readable benchmark results.
- `docs/lightgbm_tuning_validation_results.csv` - training-only tuning screen.
- `docs/optimised_lightgbm_feature_importance.csv` - final feature-importance values.
- `docs/decisions/2026-week-7-model-choice.md` - decision journal.
- `docs/linkedin_week7_update.md` - required LinkedIn paragraph.
- `docs/figures/` - model comparison, timing, confusion-matrix and feature-importance figures.

## Models compared

1. Logistic regression
2. Bounded decision tree
3. Random forest
4. Base LightGBM
5. Base XGBoost
6. Optimised LightGBM

## Main finding

The optimised LightGBM model achieved **66.4% accuracy**, **0.518 macro F1** and **25.0% ESI Level 1 recall**. It provided the strongest balanced score while maintaining low measured compute cost, but its patient-level interpretability remains weaker than logistic regression.

## Data governance

The patient-level dataset is not included in this public submission. Only aggregate metrics, figures, reports and the executed notebook are committed.
