# Week 5 Final Submission - AI-Assisted Triage Data Exploration

## Contents

- `notebooks/week5_final_exploration.ipynb` - commented exploration pipeline.
- `docs/feasibility_memo.pdf` - 3-page ED Board feasibility memo.
- `docs/feasibility_memo.md` - editable markdown version of the memo.
- `docs/figures/` - dashboard and supporting figures.
- `docs/missingness_table.csv` - missingness table.
- `docs/outlier_table.csv` - vital-sign outlier audit table.
- `docs/top_chief_complaints.csv` - top chief complaints.
- `docs/top_10_feature_shortlist.csv` - ranked top-10 feature shortlist.

## Verdict

Proceed with caveats. The dataset is suitable for offline baseline modelling, but not clinical deployment until leakage variables are removed, extreme values are reviewed, and subgroup performance is validated.

## Data note

The dataset file should remain local/private because it is healthcare data, even if de-identified.
Do not commit raw patient-level CSV files to a public GitHub repository.

Expected local file for the notebook:

```text
data/yaleemmlc_admissionprediction_triage.csv
```

or place it in the same folder as the notebook and update `DATA_PATH`.

## GitHub structure

```text
docs/
  feasibility_memo.pdf
  feasibility_memo.md
  figures/
  missingness_table.csv
  outlier_table.csv
  top_chief_complaints.csv
  top_10_feature_shortlist.csv

notebooks/
  week5_final_exploration.ipynb
```
