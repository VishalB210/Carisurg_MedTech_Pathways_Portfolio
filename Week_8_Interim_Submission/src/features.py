"""Feature selection and modelling-matrix helpers."""

from __future__ import annotations

from collections.abc import Iterable

import pandas as pd


def select_feature_columns(
    frame: pd.DataFrame,
    *,
    target: str,
    excluded_columns: Iterable[str],
) -> list[str]:
    """Return numeric, pre-triage feature columns after exclusions."""
    excluded = set(excluded_columns) | {target}
    candidates = [column for column in frame.columns if column not in excluded]
    numeric = [
        column
        for column in candidates
        if pd.api.types.is_numeric_dtype(frame[column])
    ]
    if not numeric:
        raise ValueError("No numeric model features remain after exclusions.")
    return numeric


def split_features_target(
    frame: pd.DataFrame,
    *,
    target: str,
    excluded_columns: Iterable[str],
) -> tuple[pd.DataFrame, pd.Series, list[str]]:
    """Create X, y, and the ordered feature-name list."""
    feature_columns = select_feature_columns(
        frame,
        target=target,
        excluded_columns=excluded_columns,
    )
    X = frame.loc[:, feature_columns].copy()
    y = frame.loc[:, target].astype(int).copy()

    if X.isna().any().any():
        raise ValueError("The model matrix still contains missing values after cleaning.")
    return X, y, feature_columns
