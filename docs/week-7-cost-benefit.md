# Week 7 Cost-Benefit Memo - Revised

**To:** Dr. De Fretias, ED Board, and Martina Griffith, Clinical IT Lead  
**From:** Vishal Baboolal  
**Subject:** Phase 3 model choice for AI-assisted emergency triage  
**Date:** 2026

## 1. Verdict

Advance the optimised LightGBM model to a silent Phase 3 pilot, retain logistic regression as the transparent reference, and keep both away from live clinical decisions.

## 2. Dataset and methods recap

The comparison used the same cleaned dataset and 80/20 stratified split from Week 6 (`random_state=42`): 55,121 encounters and 208 numeric pre-triage features. Post-triage outcomes, administrative identifiers, and fairness-sensitive demographic variables were excluded. Logistic regression and a bounded decision tree were retained; random forest, LightGBM, and XGBoost were screened. LightGBM was tuned on a training-only validation split, with the final test set reserved for evaluation.

## 3. Benchmark

| Model | Accuracy | Macro F1 | ESI 1 recall | Train (s) | Inference (ms) | Explainable in under 1 minute? |
|---|---:|---:|---:|---:|---:|:--:|
| Logistic regression | 0.667 | 0.492 | 0.250 | 13.581 | 0.0103 | **YES** |
| Random forest | 0.497 | 0.398 | 0.500 | 7.301 | 0.0235 | **NO** |
| LightGBM base | 0.673 | 0.472 | 0.125 | 2.456 | 0.0325 | **NO** |
| XGBoost base | 0.614 | 0.377 | 0.188 | 3.566 | 0.0075 | **NO** |
| **Optimised LightGBM** | **0.664** | **0.518** | **0.250** | **3.908** | **0.0574** | **NO** |

The verdict refers to whether the native model can support a meaningful patient-level explanation within one minute. Global importance alone does not satisfy that standard.

## 4. Arguments for the recommendation

1. Best balance across ESI levels: macro F1 improved from 0.492 for logistic regression to 0.518.
2. Acceptable compute cost: measured training and per-patient inference were operationally small for a silent pilot.
3. Practical modelling capacity: LightGBM captures non-linear relationships while remaining easier to operate than a neural network.

## 5. Arguments against the recommendation

1. Lower transparency: it fails the native under-one-minute patient-level explanation test.
2. Limited gain: ESI Level 1 recall did not improve above logistic regression in this held-out set.
3. Higher maintenance: an additional package, hyperparameters, versioning, explanation tooling, and monitoring are required.

## 6. Risks and unknowns

Only 16 ESI Level 1 cases were present in the held-out test set, so critical-class estimates are unstable. Timing was measured on one runtime, not Mercer infrastructure. Fairness, calibration, drift, missing-data behaviour, local Caribbean transferability, alert burden, and patient-level explanation quality remain untested.

## 7. Recommendation

Proceed only with a silent pilot beside logistic regression. Compare critical-class errors, subgroup performance, calibration, latency, and explanation usability on local data. Do not expose predictions to triage staff or use them for prioritisation until the evidence is stronger and the explanation approach is clinically approved.
