# Week 8 Handover Draft - AI-Assisted Emergency Department Triage

## Project summary

This repository contains a reproducible research pipeline for predicting Emergency Severity Index (ESI) levels 1-5 from de-identified, pre-triage clinical variables. The work is intended only for offline and silent-pilot evaluation. The modular code loads the governed Week 5 cleaned dataset, applies the documented feature exclusions, creates the same seeded stratified split used in Weeks 6-7, trains the pinned model from one configuration file, and saves the model plus audit metrics.

## Final model decision

**Optimised LightGBM is the pinned final model.** It won because it achieved the strongest Week 7 macro F1 (0.518) while maintaining accuracy close to logistic regression and low measured compute cost. Logistic regression remains the transparent reference model, and neither model should influence live triage decisions.

## How to run

```bash
git clone <PUBLIC-REPOSITORY-URL>
cd Carisurg_MedTech_Pathways_Portfolio/Week_8_Interim_Submission
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
# Place the private file at data/data_cleaned_week5.csv
pytest -q
python scripts/train.py --config config.yaml
```

Expected outputs are written to `artifacts/` and `outputs/`.

## Data location and governance

The patient-level dataset is stored outside the public repository and must be supplied locally as `data/data_cleaned_week5.csv`. It is de-identified research data, but it is still governed clinical data and must not be redistributed. The public repository contains code, aggregate metrics, documentation, and non-identifiable results only.

## Known limitations

- The held-out test set contained only 16 ESI Level 1 cases, so critical-class estimates are unstable.
- Fairness, calibration, missing-data behaviour, drift, and transferability to a Caribbean emergency department remain unvalidated.
- Global LightGBM feature importance does not provide a complete patient-level explanation, so the model is not approved for live clinical use.

## Who to ask

- **Model and code:** Vishal Baboolal, project author.
- **Clinical interpretation and workflow:** Dr. De Fretias / designated ED clinical lead.
- **Data access, governance, and deployment:** Martina Griffith / Mercer Clinical IT.
