# Handover - AI-Assisted Emergency Department Triage

## Project summary

This repository contains an audit-ready research pipeline for predicting Emergency Severity Index (ESI) levels 1-5 from de-identified, pre-triage clinical variables. The canonical solution is implemented in the root-level `src/` package and driven by one `config.yaml` file. It loads the governed Week 5 cleaned dataset, applies documented exclusions, creates a seeded stratified train/test split, trains the pinned model, and writes the model bundle and aggregate evaluation outputs. Historical weekly directories are retained only as assessment evidence; a new hire does not need them to run the final pipeline.

## Final model decision

**Optimised LightGBM is the pinned final model.** It produced the strongest Week 7 macro F1 (0.518), with competitive accuracy and low measured compute time. It does **not** pass the native under-one-minute patient-level interpretability test; therefore, logistic regression remains the transparent reference and LightGBM is restricted to offline research or silent-pilot evaluation.

## How to run

```bash
git clone https://github.com/VishalB210/Carisurg_MedTech_Pathways_Portfolio.git
cd Carisurg_MedTech_Pathways_Portfolio
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -q
# Place the governed file at data/data_cleaned_week5.csv
python scripts/train.py --config config.yaml
```

The pipeline writes the trained bundle to `artifacts/` and aggregate audit outputs to `outputs/`.

## Data location and governance

The patient-level dataset is stored outside the public repository and must be supplied locally as `data/data_cleaned_week5.csv`. It is governed clinical research data and must not be redistributed. The public repository contains code, documentation, aggregate metrics, and non-identifiable results only.

## Known limitations

- The Week 7 held-out set contained only 16 ESI Level 1 cases, so critical-class estimates are unstable.
- Fairness, calibration, missing-data behaviour, drift, and transferability to a Caribbean emergency department remain unvalidated.
- Optimised LightGBM cannot natively provide a reliable patient-level explanation in under one minute; a validated explanation layer and clinical review are required before any operational use.
