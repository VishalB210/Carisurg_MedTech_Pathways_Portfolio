#!/usr/bin/env python3
"""Single entry point for training the pinned Week 8 model."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from sklearn.model_selection import train_test_split

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.data import clean_data, load_data, validate_schema  # noqa: E402
from src.features import split_features_target  # noqa: E402
from src.model import build_model, evaluate_model, save_model_bundle, train_model  # noqa: E402
from src.utils import load_config, resolve_project_path, save_json, set_seed  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config",
        default="config.yaml",
        help="Path to the YAML configuration file (default: config.yaml).",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Optional row limit for a quick local check. Do not use for final metrics.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = load_config(args.config)

    seed = int(config["seed"])
    set_seed(seed)

    target = str(config["data"]["target"])
    labels = [int(value) for value in config["data"]["valid_labels"]]
    data_path = resolve_project_path(config["data"]["path"])

    frame = load_data(data_path)
    if args.limit is not None:
        if args.limit < 10:
            raise ValueError("--limit must be at least 10 rows.")
        frame = frame.head(args.limit).copy()

    frame = clean_data(frame, target=target)
    validate_schema(
        frame,
        target=target,
        required_columns=config["data"]["required_columns"],
        valid_labels=labels,
    )

    excluded = (
        config["features"]["demographics"]
        + config["features"]["administrative"]
        + config["features"]["leakage"]
    )
    X, y, feature_names = split_features_target(
        frame,
        target=target,
        excluded_columns=excluded,
    )

    split = config["split"]
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=float(split["test_size"]),
        stratify=y,
        random_state=seed,
    )

    model = build_model(config["model"], seed=seed)
    training_seconds = train_model(model, X_train, y_train)
    metrics, report, matrix = evaluate_model(
        model,
        X_test,
        y_test,
        labels=labels,
    )
    metrics["training_time_seconds"] = float(training_seconds)
    metrics["training_rows"] = int(len(X_train))
    metrics["feature_count"] = int(len(feature_names))
    metrics["model"] = "Optimised LightGBM"

    model_path = resolve_project_path(config["outputs"]["model_path"])
    metrics_path = resolve_project_path(config["outputs"]["metrics_path"])
    report_path = resolve_project_path(config["outputs"]["classification_report_path"])
    matrix_path = resolve_project_path(config["outputs"]["confusion_matrix_path"])

    save_model_bundle(
        model,
        feature_names=feature_names,
        model_path=model_path,
        metadata={"seed": seed, "target": target, "labels": labels},
    )
    save_json(metrics, metrics_path)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report.to_csv(report_path)
    matrix_path.parent.mkdir(parents=True, exist_ok=True)
    import pandas as pd

    pd.DataFrame(matrix, index=labels, columns=labels).to_csv(matrix_path)

    print("Training completed.")
    print(f"Model: {metrics['model']}")
    print(f"Accuracy: {metrics['accuracy']:.4f}")
    print(f"Macro F1: {metrics['macro_f1']:.4f}")
    print(f"ESI Level 1 recall: {metrics['esi_1_recall']:.4f}")
    print(f"Saved model bundle: {model_path}")
    print(f"Saved metrics: {metrics_path}")


if __name__ == "__main__":
    main()
