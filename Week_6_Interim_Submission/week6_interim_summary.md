# Week 6 Interim Submission — Baseline Triage Model

**Student:** Vishal Baboolal  
**Project:** AI-Assisted Emergency Department Triage  
**Random seed:** `42`

## Interim objective

Train at least one defensible baseline classifier using the cleaned Week 5 dataset, evaluate it on a held-out test set, and produce an initial confusion matrix.

## Dataset and modelling setup

- Records: **55,121**
- Original columns: **225**
- Model input features: **208 numeric clinical features**
- Target: **Emergency Severity Index (`esi`)**, levels 1–5
- Train/test split: **80/20**
- Stratification: **Yes, by ESI level**
- Training records: **44,096**
- Test records: **11,025**
- Excluded leakage variables: `disposition`, `previousdispo`
- Excluded administrative and fairness-sensitive demographic fields from this first baseline

## Initial results

| Model | Accuracy | Macro F1 | Weighted F1 | ESI 1 recall |
|---|---:|---:|---:|---:|
| Stratified random baseline | 0.375 | 0.204 | 0.375 | 0.000 |
| Logistic regression | 0.667 | 0.492 | 0.661 | 0.250 |

The logistic regression substantially outperformed the stratified random baseline on overall accuracy. However, performance for the rare and clinically critical ESI Level 1 class remained weak. Of **16** true ESI 1 patients in the test set, the model correctly identified **4** and missed **12**, giving an ESI 1 recall of **25.0%**.

## Clinical interpretation

The most important early safety concern is under-triage of ESI Level 1 patients. A false negative at this level means a patient who requires immediate resuscitation could be assigned a less urgent category. For that reason, **ESI Level 1 recall** will be treated as the primary clinical safety metric, while accuracy, macro F1, weighted F1, and the confusion matrix will be reported as supporting measures.

## Interim conclusion

The model beats a random-guess baseline, so the dataset contains useful predictive signal. The current model is **not suitable for clinical deployment**, because it misses most ESI Level 1 cases. The next stage should compare the logistic regression with a bounded decision tree, examine failure modes, and assess whether class weighting or other defensible adjustments improve identification of critically ill patients without creating excessive false alarms.

## Files

- `notebooks/week6_interim_baseline_model.ipynb`
- `docs/week6/logistic_regression_confusion_matrix.png`
- `docs/week6/initial_model_metrics.csv`
- `docs/week6/logistic_regression_classification_report.csv`
