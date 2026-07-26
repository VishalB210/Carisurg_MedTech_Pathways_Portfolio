"""End-to-end training smoke test on approximately 50 synthetic rows."""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from src.data import clean_data, validate_schema
from src.features import split_features_target
from src.model import build_model, evaluate_model, train_model


def test_training_pipeline_smoke_test_on_50_rows() -> None:
    rng = np.random.default_rng(42)
    labels = np.repeat([1, 2, 3, 4, 5], 10)
    frame = pd.DataFrame(
        {
            "esi": labels,
            "triage_vital_hr": rng.normal(90 + labels * 2, 5),
            "triage_vital_sbp": rng.normal(125 - labels, 8),
            "triage_vital_dbp": rng.normal(80, 5, 50),
            "triage_vital_temp": rng.normal(37.0, 0.5, 50),
            "triage_vital_rr": rng.normal(18 + labels * 0.3, 2),
            "triage_vital_o2": rng.normal(98 - labels * 0.2, 1),
            "triage_glucose": rng.normal(5.5 + labels * 0.1, 0.5),
            "cc_chestpain": rng.integers(0, 2, 50),
            "age": rng.integers(18, 90, 50),
            "disposition": ["excluded"] * 50,
        }
    )

    cleaned = clean_data(frame, target="esi")
    required = [
        "triage_vital_hr",
        "triage_vital_sbp",
        "triage_vital_dbp",
        "triage_vital_temp",
        "triage_vital_rr",
        "triage_vital_o2",
        "triage_glucose",
    ]
    validate_schema(
        cleaned,
        target="esi",
        required_columns=required,
        valid_labels=[1, 2, 3, 4, 5],
    )
    X, y, _ = split_features_target(
        cleaned,
        target="esi",
        excluded_columns=["age", "disposition"],
    )
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        stratify=y,
        random_state=42,
    )

    model = build_model(
        {
            "name": "lightgbm",
            "params": {
                "objective": "multiclass",
                "num_class": 5,
                "n_estimators": 5,
                "learning_rate": 0.1,
                "num_leaves": 7,
                "min_child_samples": 2,
                "class_weight": {1: 2.0, 2: 1.2, 3: 1.0, 4: 1.2, 5: 1.5},
            },
        },
        seed=42,
    )
    elapsed = train_model(model, X_train, y_train)
    metrics, report, matrix = evaluate_model(
        model,
        X_test,
        y_test,
        labels=[1, 2, 3, 4, 5],
    )

    assert elapsed >= 0
    assert 0.0 <= metrics["accuracy"] <= 1.0
    assert 0.0 <= metrics["macro_f1"] <= 1.0
    assert report.shape[0] >= 5
    assert matrix.shape == (5, 5)
