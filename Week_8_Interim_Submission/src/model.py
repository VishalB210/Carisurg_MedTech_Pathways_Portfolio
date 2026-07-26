"""Model construction, training, evaluation, and persistence."""

from __future__ import annotations

import time
from pathlib import Path
from typing import Any

import joblib
import numpy as np
import pandas as pd
from lightgbm import LGBMClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)


def build_model(model_config: dict[str, Any], *, seed: int) -> LGBMClassifier:
    """Build the single pinned Week 8 LightGBM model from configuration."""
    model_name = str(model_config.get("name", "")).lower()
    if model_name not in {"lightgbm", "lgbm", "lgbmclassifier"}:
        raise ValueError(
            "Week 8 is pinned to one final model. Expected model.name='lightgbm'."
        )

    params = dict(model_config.get("params", {}))
    params.setdefault("random_state", seed)
    params.setdefault("n_jobs", -1)
    params.setdefault("verbosity", -1)

    class_weight = params.get("class_weight")
    if isinstance(class_weight, dict):
        params["class_weight"] = {int(key): float(value) for key, value in class_weight.items()}

    return LGBMClassifier(**params)


def train_model(model: LGBMClassifier, X_train: pd.DataFrame, y_train: pd.Series) -> float:
    """Fit the model and return wall-clock training time in seconds."""
    started = time.perf_counter()
    model.fit(X_train, y_train)
    return time.perf_counter() - started


def evaluate_model(
    model: LGBMClassifier,
    X_test: pd.DataFrame,
    y_test: pd.Series,
    *,
    labels: list[int],
) -> tuple[dict[str, Any], pd.DataFrame, np.ndarray]:
    """Evaluate the fitted classifier using the Week 7 audit metrics."""
    started = time.perf_counter()
    predictions = model.predict(X_test)
    inference_seconds = time.perf_counter() - started

    metrics: dict[str, Any] = {
        "accuracy": float(accuracy_score(y_test, predictions)),
        "macro_precision": float(
            precision_score(y_test, predictions, average="macro", zero_division=0)
        ),
        "macro_recall": float(
            recall_score(y_test, predictions, average="macro", zero_division=0)
        ),
        "macro_f1": float(f1_score(y_test, predictions, average="macro", zero_division=0)),
        "weighted_f1": float(
            f1_score(y_test, predictions, average="weighted", zero_division=0)
        ),
        "inference_time_seconds": float(inference_seconds),
        "inference_time_per_prediction_ms": float(
            inference_seconds / max(len(X_test), 1) * 1000
        ),
        "test_rows": int(len(X_test)),
    }

    per_class_recall = recall_score(
        y_test,
        predictions,
        labels=labels,
        average=None,
        zero_division=0,
    )
    for label, value in zip(labels, per_class_recall, strict=True):
        metrics[f"esi_{label}_recall"] = float(value)

    report = pd.DataFrame(
        classification_report(
            y_test,
            predictions,
            labels=labels,
            output_dict=True,
            zero_division=0,
        )
    ).transpose()
    matrix = confusion_matrix(y_test, predictions, labels=labels)
    return metrics, report, matrix


def save_model_bundle(
    model: LGBMClassifier,
    *,
    feature_names: list[str],
    model_path: str | Path,
    metadata: dict[str, Any] | None = None,
) -> None:
    """Persist the trained model together with its ordered feature contract."""
    path = Path(model_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(
        {
            "model": model,
            "feature_names": feature_names,
            "metadata": metadata or {},
        },
        path,
    )
