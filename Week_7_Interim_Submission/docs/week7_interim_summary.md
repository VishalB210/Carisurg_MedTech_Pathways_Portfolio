# Week 7 Interim Summary

## Objective

Train a more sophisticated model using the same Week 6 data split and compare it honestly with the Week 6 baselines across performance, compute cost and interpretability.

## Model choice

A **Random Forest** was selected because it is well suited to tabular clinical data, captures non-linear relationships and provides global feature importance. It is also easier to govern than a neural network, although less directly interpretable than logistic regression or a single decision tree.

## Configuration

- `n_estimators=200`
- `max_depth=20`
- `min_samples_leaf=5`
- `max_features="sqrt"`
- `class_weight="balanced_subsample"`
- `random_state=42`
- `n_jobs=1` for auditable single-core timing

## Initial result

The random forest achieved:

- Accuracy: **0.497**
- Macro precision: **0.407**
- Macro recall: **0.557**
- Macro F1: **0.398**
- ESI Level 1 recall: **0.500**
- Training time: **9.324 seconds**
- Inference time: **0.0222 ms per patient**

The Week 6 logistic-regression baseline achieved **0.667 accuracy**, **0.492 macro F1** and **0.250 ESI Level 1 recall**.

## Interim trade-off

The random forest caught a greater proportion of the rare ESI Level 1 patients, but overall accuracy and macro F1 were lower. This indicates a genuine safety-versus-efficiency trade-off rather than a clear winner. Further tuning and error analysis will be needed before the final Phase 3 recommendation.

## Data governance

The patient-level dataset is excluded from the public repository. Only aggregate metrics, figures, model outputs and the executed notebook are included.
