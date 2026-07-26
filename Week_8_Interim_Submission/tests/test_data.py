"""Schema-contract sanity checks."""

import pandas as pd
import pytest

from src.data import clean_data, validate_schema


REQUIRED = [
    "triage_vital_hr",
    "triage_vital_sbp",
    "triage_vital_dbp",
    "triage_vital_temp",
    "triage_vital_rr",
    "triage_vital_o2",
    "triage_glucose",
]


def test_data_loader_schema_contract() -> None:
    frame = pd.DataFrame(
        {
            "esi": [1, 2, 3, 4, 5, 9],
            "triage_vital_hr": [90, 88, 100, 76, 82, 91],
            "triage_vital_sbp": [120, 118, 130, 125, 119, 121],
            "triage_vital_dbp": [80, 78, 85, 81, 79, 82],
            "triage_vital_temp": [37.0, 36.9, 38.0, 37.2, 36.8, 37.1],
            "triage_vital_rr": [18, 17, 20, 19, 16, 18],
            "triage_vital_o2": [99, 98, 95, 97, 99, 98],
            "triage_glucose": [5.4, 6.1, None, 5.8, 5.3, 5.7],
        }
    )

    cleaned = clean_data(frame, target="esi")
    validate_schema(
        cleaned,
        target="esi",
        required_columns=REQUIRED,
        valid_labels=[1, 2, 3, 4, 5],
    )

    assert set(cleaned["esi"].unique()) == {1, 2, 3, 4, 5}
    assert cleaned[REQUIRED].isna().sum().sum() == 0


def test_schema_check_fails_when_required_column_is_missing() -> None:
    frame = pd.DataFrame({"esi": [1, 2, 3], "triage_vital_hr": [80, 90, 100]})
    with pytest.raises(ValueError, match="Missing required columns"):
        validate_schema(
            frame,
            target="esi",
            required_columns=REQUIRED,
            valid_labels=[1, 2, 3, 4, 5],
        )
