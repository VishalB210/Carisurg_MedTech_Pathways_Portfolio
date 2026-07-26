"""Data loading, cleaning, and schema validation utilities."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable, Sequence

import numpy as np
import pandas as pd


VALID_ESI_LEVELS = {1, 2, 3, 4, 5}


def load_data(path: str | Path) -> pd.DataFrame:
    """Load a CSV dataset from *path* and fail with an actionable error."""
    data_path = Path(path)
    if not data_path.exists():
        raise FileNotFoundError(
            f"Dataset not found at '{data_path}'. Place the private cleaned CSV "
            "there or update data.path in config.yaml."
        )
    if data_path.suffix.lower() != ".csv":
        raise ValueError(f"Expected a CSV file, received: {data_path.suffix or 'no suffix'}")

    frame = pd.read_csv(data_path)
    if frame.empty:
        raise ValueError("The loaded dataset is empty.")
    return frame


def clean_data(
    frame: pd.DataFrame,
    *,
    target: str = "esi",
    numeric_prefixes: Sequence[str] = ("triage_", "cc_"),
) -> pd.DataFrame:
    """Apply conservative cleaning while preserving the Week 5 logic.

    The Week 5 CSV is already the governed cleaned modelling source. This function
    therefore performs only reproducibility safeguards: trims column names,
    coerces the target and clinical numeric columns, drops invalid ESI rows,
    replaces infinite values, and median-imputes numeric columns.
    """
    if frame.empty:
        raise ValueError("Cannot clean an empty DataFrame.")

    cleaned = frame.copy()
    cleaned.columns = [str(column).strip() for column in cleaned.columns]

    if target not in cleaned.columns:
        raise ValueError(f"Target column '{target}' is missing.")

    cleaned[target] = pd.to_numeric(cleaned[target], errors="coerce")
    cleaned = cleaned[cleaned[target].isin(VALID_ESI_LEVELS)].copy()
    cleaned[target] = cleaned[target].astype(int)

    for column in cleaned.columns:
        if column == target:
            continue
        should_be_numeric = (
            pd.api.types.is_numeric_dtype(cleaned[column])
            or any(column.startswith(prefix) for prefix in numeric_prefixes)
        )
        if should_be_numeric:
            cleaned[column] = pd.to_numeric(cleaned[column], errors="coerce")

    numeric_columns = cleaned.select_dtypes(include=[np.number]).columns.tolist()
    if numeric_columns:
        cleaned[numeric_columns] = cleaned[numeric_columns].replace([np.inf, -np.inf], np.nan)
        feature_numeric_columns = [column for column in numeric_columns if column != target]
        for column in feature_numeric_columns:
            if cleaned[column].isna().all():
                cleaned[column] = 0.0
            elif cleaned[column].isna().any():
                cleaned[column] = cleaned[column].fillna(cleaned[column].median())

    if cleaned.empty:
        raise ValueError("No rows remain after removing invalid ESI values.")
    return cleaned


def validate_schema(
    frame: pd.DataFrame,
    *,
    target: str,
    required_columns: Iterable[str],
    valid_labels: Iterable[int] = VALID_ESI_LEVELS,
) -> None:
    """Validate the minimum schema contract required by the model pipeline."""
    required = list(dict.fromkeys([target, *required_columns]))
    missing = [column for column in required if column not in frame.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    if frame.empty:
        raise ValueError("Dataset contains no rows.")

    allowed = set(valid_labels)
    observed = set(pd.Series(frame[target]).dropna().astype(int).unique().tolist())
    invalid = sorted(observed - allowed)
    if invalid:
        raise ValueError(f"Target '{target}' contains invalid labels: {invalid}")

    if frame[target].isna().any():
        raise ValueError(f"Target '{target}' contains missing values.")
