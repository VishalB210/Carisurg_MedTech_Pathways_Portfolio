# Decision Journal - 2026 Week 7 Model Choice

## Context

- The ED Board asked whether a more sophisticated model provides enough benefit to justify lower interpretability and higher operational complexity.
- Mercer IT Governance requested measured training time, inference time and a realistic view of deployment cost.

## Alternatives considered

- Retain logistic regression as the Phase 3 model.
- Advance the random forest because it identified a larger proportion of ESI Level 1 cases in this test set.
- Advance an optimised LightGBM model after comparing random forest, LightGBM and XGBoost base performance.

## Decision

**Advance the optimised LightGBM model to a silent Phase 3 pilot, while retaining logistic regression as the transparent reference model and keeping both away from live clinical decisions.**

## Reasoning

- Optimised LightGBM produced the strongest macro F1 in the final comparison while keeping accuracy close to logistic regression.
- Its measured training and inference times were operationally small for a silent pilot.
- Its interpretability is weaker than logistic regression, but global feature importance and side-by-side reference-model comparison make governance review possible.

## Things I do not yet know

- Whether the measured improvement will hold on local Caribbean emergency department data and across demographic subgroups.
- Whether clinicians will find patient-level explanations from a boosted model sufficiently clear for safe workflow integration.

## Revisit trigger

Revisit this decision after local silent-pilot evidence is available, especially ESI Level 1 and ESI Level 2 error analysis, subgroup performance, calibration and production latency.
