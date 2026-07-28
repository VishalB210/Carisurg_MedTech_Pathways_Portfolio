# CariSurg MedTech Pathways 2026 - AI-Assisted Emergency Department Triage

**Student:** Vishal Baboolal  
**Final model:** Optimised LightGBM  
**Intended use:** Offline research and silent-pilot evaluation only

## Project overview

This repository documents the development of an AI-assisted emergency-department triage research pipeline. The root directory is the canonical, reproducible implementation requested for the Week 8 handover. Historical `Week_*_Submission/` directories remain only as assessment and audit evidence; the runnable workflow no longer depends on them.

## Canonical root-level structure

```text
Carisurg_MedTech_Pathways_Portfolio/
├── src/                    # loading, cleaning, features, training and helpers
├── scripts/train.py        # single training entry point
├── tests/                  # schema and 50-row smoke tests
├── docs/
│   ├── HANDOVER.md
│   ├── model-selection.md
│   ├── model-selection.csv
│   ├── week-7-cost-benefit.md
│   ├── week-7-cost-benefit.pdf
│   └── decisions/
├── notebooks/              # exploratory and historical notebooks
├── data/README.md          # governed-data instructions; no patient data
├── artifacts/              # locally generated model bundle
├── outputs/                # locally generated aggregate metrics
├── config.yaml             # one pinned model configuration
├── requirements.txt        # pinned environment
└── .github/workflows/tests.yml
```

## New-hire quick start

Python 3.11 or later is recommended.

```bash
git clone https://github.com/VishalB210/Carisurg_MedTech_Pathways_Portfolio.git
cd Carisurg_MedTech_Pathways_Portfolio
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -q
```

Place the governed cleaned dataset locally at:

```text
data/data_cleaned_week5.csv
```

Run the pinned model from the single configuration file:

```bash
python scripts/train.py --config config.yaml
```

The command writes the model bundle to `artifacts/` and aggregate evaluation outputs to `outputs/`.

## Final model decision

Optimised LightGBM was selected because it achieved the strongest Week 7 macro F1 (0.518) while retaining competitive accuracy and low measured compute time. The audit table now gives an explicit **under-one-minute interpretability verdict** for every model rather than subjective High/Medium labels.

- [Model-selection audit trail](docs/model-selection.md)
- [Week 7 model-choice decision journal](docs/decisions/2026-week-7-model-choice.md)
- [Revised three-page Week 7 cost-benefit memo](docs/week-7-cost-benefit.pdf)
- [Original Week 7 final deliverable folder](Week_7_Final_Submission/)

## Reproducibility safeguards

- One model, one random seed, and one hyperparameter set are committed in `config.yaml`.
- Library versions are pinned in `requirements.txt`.
- `tests/` contains a schema-loading check and a 50-row training smoke test.
- The optional GitHub Actions workflow runs `pytest` after pushes and pull requests.
- Governed patient-level data and generated model artefacts are excluded through `.gitignore`.

## Governance and limitations

This work is not a clinical device and must not influence live triage decisions. The dataset is not included publicly. Fairness, calibration, local validation, drift monitoring, patient-level explainability, and critical-class performance require further assessment before any operational use.

See [`docs/HANDOVER.md`](docs/HANDOVER.md) for the one-page handover guide.
