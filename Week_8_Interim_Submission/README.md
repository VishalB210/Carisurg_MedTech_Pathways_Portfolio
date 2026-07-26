# Week 8 Interim Submission - Reproducibility and Modular Project Design

**Student:** Vishal Baboolal  
**Project:** AI-Assisted Emergency Department Triage  
**Pinned final model:** Optimised LightGBM  
**Intended use:** Offline research and silent-pilot evaluation only

## Interim deliverables included

- Draft modular package in `src/`, including the required `data.py` and `model.py` modules.
- Single configuration file, `config.yaml`, containing the seed, paths, exclusions, and pinned model parameters.
- Single entry point: `python scripts/train.py --config config.yaml`.
- Model-selection audit trail in `docs/model-selection.md` and `.csv`.
- One-page handover draft in `docs/HANDOVER_DRAFT.md`.
- Two pytest sanity checks in `tests/`.
- Pinned library versions in `requirements.txt`.
- Week 7 notebook and decision reference retained under `notebooks/` and `docs/`.

## Repository layout

```text
Week_8_Interim_Submission/
├── config.yaml
├── requirements.txt
├── README.md
├── src/
│   ├── __init__.py
│   ├── data.py
│   ├── features.py
│   ├── model.py
│   └── utils.py
├── scripts/
│   └── train.py
├── tests/
│   ├── test_data.py
│   └── test_training.py
├── docs/
│   ├── model-selection.md
│   ├── model-selection.csv
│   ├── HANDOVER_DRAFT.md
│   └── INTERIM_SUBMISSION_CHECKLIST.md
├── notebooks/
│   └── week7_final_model_optimisation.ipynb
├── data/
│   └── README.md
├── artifacts/
└── outputs/
```

## New-hire quick start

Python 3.10 or later is recommended.

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -q
```

To run the full pipeline, place the private cleaned file at:

```text
data/data_cleaned_week5.csv
```

Then run:

```bash
python scripts/train.py --config config.yaml
```

The pipeline saves a model bundle to `artifacts/` and audit outputs to `outputs/`.

## Model decision

The Week 7 recommendation was to advance optimised LightGBM to a silent Phase 3 pilot while retaining logistic regression as the transparent reference. The winner achieved 0.664 accuracy and 0.518 macro F1 on the held-out test set. The full comparison is in [`docs/model-selection.md`](docs/model-selection.md).

## Important interim validation note

The uploaded Week 7 package preserved the benchmark results and documented the winner as a regularised, moderately class-weighted LightGBM model, but it did not preserve the complete estimator-constructor code. This interim package therefore freezes an explicit, defensible parameter set in `config.yaml`. Before the final Tuesday submission, run the private dataset once and compare the produced metrics with the Week 7 benchmark; adjust only if necessary to reproduce the original run, then keep the confirmed values pinned.

## Data governance

The patient-level dataset is intentionally excluded from this public repository. Do not upload it. The `.gitignore` blocks common data files under `data/`.
