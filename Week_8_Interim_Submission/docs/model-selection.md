# Model-Selection Audit Trail - Weeks 6-7

**Winner: Optimised LightGBM**  
**Decision:** Advance it only to a silent Phase 3 pilot, while retaining logistic regression as the transparent reference.  
**Full reasoning:** [Week 7 decision journal](../../Week_7_Final_Submission/docs/decisions/2026-week-7-model-choice.md)

| Winner | Model | Key hyperparameters / setup | Accuracy | Macro precision | Macro recall | Macro F1 | ESI 1 recall | Training time (s) | Inference per prediction (ms) |
|:--:|---|---|---:|---:|---:|---:|---:|---:|---:|
|  | Logistic Regression | StandardScaler; `max_iter=1000`; `random_state=42` | 0.6668 | 0.5825 | 0.4630 | 0.4925 | 0.2500 | 13.5813 | 0.0103 |
|  | Decision Tree | `max_depth=12`; `random_state=42` | 0.5848 | 0.4806 | 0.2948 | 0.3027 | 0.0625 | 0.3681 | 0.0010 |
|  | Random Forest | `n_estimators=200`; `class_weight=balanced_subsample`; `random_state=42` | 0.4965 | 0.4074 | 0.5568 | 0.3984 | 0.5000 | 7.3006 | 0.0235 |
|  | LightGBM Base | Base `LGBMClassifier`; `random_state=42` | 0.6726 | 0.5890 | 0.4363 | 0.4718 | 0.1250 | 2.4561 | 0.0325 |
|  | XGBoost Base | Base `XGBClassifier`; `random_state=42` | 0.6140 | 0.5785 | 0.3504 | 0.3768 | 0.1875 | 3.5657 | 0.0075 |
| **YES** | **Optimised LightGBM** | `n_estimators=300`; `learning_rate=0.05`; `max_depth=10`; regularisation; moderate clinical class weights; `random_state=42` | **0.6642** | **0.5214** | **0.5156** | **0.5180** | **0.2500** | **3.9082** | **0.0574** |

## Audit note

The performance and timing values above are copied from the committed Week 7 benchmark. The Week 7 package documented the winning family as regularised and moderately class-weighted, but it did not preserve the full estimator-constructor code. Week 8 therefore freezes the explicit constructor values in `config.yaml`. Before the final Tuesday submission, rerun the private dataset once and confirm that the refactored pipeline reproduces the Week 7 metrics within normal runtime tolerance.
