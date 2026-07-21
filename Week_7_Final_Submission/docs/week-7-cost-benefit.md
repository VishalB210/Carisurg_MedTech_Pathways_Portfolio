# Week 7 Cost-Benefit Memo

**To:** Dr. De Fretias, ED Board, and Martina Griffith, Clinical IT Lead  
**From:** Vishal Baboolal  
**Subject:** Phase 3 model choice for AI-assisted emergency triage  
**Date:** 2026

## Verdict

**Advance the optimised LightGBM model to a silent Phase 3 pilot, while retaining logistic regression as the transparent reference model and keeping both away from live clinical decisions.**

## Dataset and methods recap

The comparison used the same cleaned dataset and the same 80/20 stratified train-test split from Week 6, with `random_state=42`. The dataset contains **55,121 emergency department encounters**, and the modelling matrix contains **208 numeric clinical features**. Post-triage outcome variables, administrative identifiers, and fairness-sensitive demographic variables were excluded from the clinical baseline.

The Week 6 logistic-regression and bounded decision-tree models were retained. Three more sophisticated approaches were then screened: random forest, LightGBM and XGBoost. LightGBM produced the strongest base accuracy among the complex models and was therefore optimised on a training-only validation split. The optimisation adjusted class weights and regularisation to improve performance across all five ESI levels without using the final test set for model selection.

## Benchmark

| Model | Accuracy | Macro F1 | ESI 1 recall | Training time | Inference per patient | Interpretability |
|---|---:|---:|---:|---:|---:|---|
| Logistic regression | 0.667 | 0.492 | 0.250 | 13.581 s | 0.0103 ms | High |
| Random forest | 0.497 | 0.398 | 0.500 | 7.301 s | 0.0235 ms | Medium |
| LightGBM base | 0.673 | 0.472 | 0.125 | 2.456 s | 0.0325 ms | Medium |
| XGBoost base | 0.614 | 0.377 | 0.188 | 3.566 s | 0.0075 ms | Medium |
| **Optimised LightGBM** | **0.664** | **0.518** | **0.250** | **3.908 s** | **0.0574 ms** | Medium |

Macro F1 gives equal importance to all ESI levels. It is useful here because the rare classes would otherwise have little influence on an overall score.

## Three arguments for the recommendation

1. **Better balance across ESI levels.** The optimised LightGBM achieved a macro F1 of **0.518**, compared with **0.492** for logistic regression. It achieved this while maintaining similar overall accuracy and the same measured ESI Level 1 recall.

2. **Acceptable compute cost.** Training completed in **3.908 seconds** on the measured runtime. Inference took approximately **0.0574 milliseconds per patient**. This is slower than logistic regression but still negligible compared with a clinical triage encounter.

3. **A practical middle ground.** LightGBM can capture non-linear interactions that logistic regression cannot, while remaining less operationally demanding than a neural network. Global feature importance can also be produced for governance review.

## Three arguments against the recommendation

1. **Reduced transparency.** Logistic regression is easier to explain to Dr. Reyes for an individual patient. A boosted ensemble combines many small trees, so one prediction is not naturally summarised by one coefficient or one decision path.

2. **Limited gain.** The improvement is meaningful but not dramatic. The optimised model did not improve ESI Level 1 recall above logistic regression in this test set, so the more complex model has not yet proved that it protects the sickest patients better.

3. **Additional maintenance.** LightGBM introduces another package, more hyperparameters, model-version controls and monitoring requirements. These costs are small during research but become important in production.

## Risks and unknowns

The ESI Level 1 test group contains only **16 patients**, so its performance estimate is unstable. Timings are wall-clock measurements from one runtime and are not a substitute for testing on Mercer infrastructure. Feature importance shows which variables influenced the model globally, but not why one specific patient received a specific triage level. Subgroup fairness, calibration, alert burden, data drift and local Caribbean transferability also remain untested.

## Recommendation

Advance the optimised LightGBM model to a **silent Phase 3 pilot only**. Run it beside logistic regression without showing predictions to triage staff. Compare errors, subgroup performance, calibration and operational latency on local data. Do not use either model for live prioritisation until the critical-class evidence is substantially stronger and patient-level explanations are reviewed with clinicians.
