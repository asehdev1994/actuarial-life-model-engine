import pandas as pd

from model.assumptions.lapse import (
    LapseSegment,
    LapseTable
)

from model.assumptions.validation import (
    validate_required_columns,
    validate_no_nulls,
    validate_numeric_columns,
    validate_rate_column,
    validate_range_columns,
    validate_no_duplicate_segments,
    validate_no_overlapping_ranges
)

REQUIRED_LAPSE_COLUMNS = [
    "product_type",
    "smoker_status",
    "duration_start",
    "duration_end",
    "lapse_rate"
]

def load_lapse_table(path):
    """
    Load lapse assumptions from CSV.

    Responsibilities:
    - read CSV
    - convert rows into structured lapse segments
    - construct LapseTable

    Does NOT:
    - perform projection logic
    - perform lapse calculations
    """

    df = pd.read_csv(path)

    validate_required_columns(
        df,
        REQUIRED_LAPSE_COLUMNS
    )

    validate_no_nulls(
        df,
        REQUIRED_LAPSE_COLUMNS
    )

    validate_numeric_columns(
        df,
        [
            "duration_start",
            "duration_end",
            "lapse_rate"
        ]
    )

    validate_rate_column(
        df,
        "lapse_rate"
    )

    validate_range_columns(
        df,
        "duration_start",
        "duration_end"
    )

    validate_no_duplicate_segments(
        df,
        [
            "product_type",
            "smoker_status",
            "duration_start",
            "duration_end"
        ]
    )

    validate_no_overlapping_ranges(
        df,
        [
            "product_type",
            "smoker_status"
        ],
        "duration_start",
        "duration_end"
    )

    segments = []

    for _, row in df.iterrows():

        segment = LapseSegment(
            product_type=row["product_type"],
            smoker_status=row["smoker_status"],
            duration_start=int(row["duration_start"]),
            duration_end=int(row["duration_end"]),
            lapse_rate=float(row["lapse_rate"])
        )

        segments.append(segment)

    return LapseTable(segments)