# Model-Selection Audit Trail - Weeks 6-7

**Winner: Optimised LightGBM**  
**Decision:** Advance it only to offline research and silent-pilot evaluation, while retaining logistic regression as the transparent reference.  
**Full reasoning:** [Week 7 model-choice decision](decisions/2026-week-7-model-choice.md)

| Winner | Model | Key hyperparameters / setup | Accuracy | Macro precision | Macro recall | Macro F1 | ESI 1 recall | Training time (s) | Inference / prediction (ms) | Under 1 minute? |
|:--:|---|---|---:|---:|---:|---:|---:|---:|---:|:--:|
|  | Logistic Regression | StandardScaler; `max_iter=1000`; `random_state=42` | 0.6668 | 0.5825 | 0.4630 | 0.4925 | 0.2500 | 13.5813 | 0.0103 | **YES** |
|  | Decision Tree | `max_depth=12`; `random_state=42` | 0.5848 | 0.4806 | 0.2948 | 0.3027 | 0.0625 | 0.3681 | 0.0010 | **YES** |
|  | Random Forest | `n_estimators=200`; balanced subsample; `random_state=42` | 0.4965 | 0.4074 | 0.5568 | 0.3984 | 0.5000 | 7.3006 | 0.0235 | **NO** |
|  | LightGBM Base | Base `LGBMClassifier`; `random_state=42` | 0.6726 | 0.5890 | 0.4363 | 0.4718 | 0.1250 | 2.4561 | 0.0325 | **NO** |
|  | XGBoost Base | Base `XGBClassifier`; `random_state=42` | 0.6140 | 0.5785 | 0.3504 | 0.3768 | 0.1875 | 3.5657 | 0.0075 | **NO** |
| **YES** | **Optimised LightGBM** | `n_estimators=300`; `learning_rate=0.05`; `num_leaves=31`; `max_depth=10`; regularisation; moderate class weights; `random_state=42` | **0.6642** | **0.5214** | **0.5156** | **0.5180** | **0.2500** | **3.9082** | **0.0574** | **NO** |

## Explicit interpretability verdicts

- **Logistic regression - YES:** coefficients and feature direction can be summarised in under one minute.
- **Decision tree - YES:** one patient prediction can normally be explained by tracing a single path in under one minute, although a depth-12 path can still be lengthy.
- **Random forest - NO:** the native ensemble is not explainable in under one minute without a post-hoc tool.
- **LightGBM and XGBoost - NO:** global importance can be generated quickly, but explaining one patient's prediction requires a validated post-hoc layer such as SHAP.
- **Optimised LightGBM - NO:** it remains the performance winner, but the lack of native under-one-minute patient-level explanation is a deployment limitation and a reason to restrict it to offline or silent-pilot use.

## Audit note

The performance and timing values are the committed Week 7 benchmark results. The canonical implementation is the root-level `src/` package, driven by the single parameter set in `config.yaml`. The historical Week 7 notebook remains in `notebooks/` for traceability but is not required to run the pipeline.
