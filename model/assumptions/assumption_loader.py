"""
Assumption ingestion layer.

Responsibilities:
- load external assumption data
- validate assumption structure
- normalise external formats
- construct structured providers

Does NOT:
- perform actuarial calculations
- perform projection logic
- perform valuation logic

Design principle:
Validation occurs only at ingestion boundaries.
"""

import pandas as pd

from model.assumptions.lapse import (
    LapseSegment,
    LapseTable
)

from model.assumptions.interest import (
    YieldCurve
)

from model.assumptions.mortality import (
    MortalityTable,
    MortalityParameters
)

from model.assumptions.assumption_validation import (
    validate_required_columns,
    validate_no_nulls,
    validate_numeric_columns,
    validate_rate_column,
    validate_range_columns,
    validate_no_duplicate_segments,
    validate_no_overlapping_ranges,
    validate_non_negative_column
)

REQUIRED_LAPSE_COLUMNS = [
    "product_type",
    "smoker_status",
    "duration_start",
    "duration_end",
    "lapse_rate"
]

REQUIRED_YIELD_CURVE_COLUMNS = [
    "t",
    "spot_rate"
]

REQUIRED_MORTALITY_COLUMNS = [
    "gender",
    "age",
    "qx"
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

def load_mortality_table(path):
    """
    Load mortality table from CSV.

    Responsibilities:
    - read CSV
    - validate mortality data
    - construct MortalityTable

    Does NOT:
    - perform projection logic
    - apply mortality improvements
    - interpolate rates
    """

    df = pd.read_csv(path)

    validate_required_columns(
        df,
        REQUIRED_MORTALITY_COLUMNS
    )

    validate_no_nulls(
        df,
        REQUIRED_MORTALITY_COLUMNS
    )

    validate_numeric_columns(
        df,
        [
            "age",
            "qx"
        ]
    )

    validate_rate_column(
        df,
        "qx"
    )

    validate_no_duplicate_segments(
        df,
        ["gender", "age"]
    )

    validate_non_negative_column(
    df,
    "age"
)

    mortality_rates = {}

    for _, row in df.iterrows():

        gender = row["gender"]
        age = int(row["age"])
        qx = float(row["qx"])

        mortality_rates[(gender, age)] = qx

    return MortalityTable(mortality_rates)

REQUIRED_MORTALITY_PARAMETER_COLUMNS = [
    "smoker_status",
    "mortality_multiplier"
]

def load_mortality_parameters(path):
    """
    Load mortality parameter assumptions.
    """

    df = pd.read_csv(path)

    validate_required_columns(
        df,
        REQUIRED_MORTALITY_PARAMETER_COLUMNS
    )

    validate_no_nulls(
        df,
        REQUIRED_MORTALITY_PARAMETER_COLUMNS
    )

    validate_numeric_columns(
        df,
        ["mortality_multiplier"]
    )

    validate_non_negative_column(
        df,
        "mortality_multiplier"
    )

    smoker_multipliers = {}

    for _, row in df.iterrows():

        smoker_status = row["smoker_status"]

        multiplier = float(
            row["mortality_multiplier"]
        )

        smoker_multipliers[
            smoker_status
        ] = multiplier

    return MortalityParameters(
        smoker_multipliers
    )

def load_yield_curve(path):
    """
    Load yield curve assumptions from CSV.

    Responsibilities:
    - read CSV
    - validate curve data
    - convert percentage rates
    - construct YieldCurve provider

    Does NOT:
    - perform interpolation
    - perform scenario modelling
    - perform valuation logic
    """

    df = pd.read_csv(path)

    validate_required_columns(
        df,
        REQUIRED_YIELD_CURVE_COLUMNS
    )

    validate_no_nulls(
        df,
        REQUIRED_YIELD_CURVE_COLUMNS
    )

    validate_numeric_columns(
        df,
        [
            "t",
            "spot_rate"
        ]
    )

    validate_non_negative_column(
        df,
        "t"
    )

    validate_no_duplicate_segments(
        df,
        ["t"]
    )

    # Convert percentages into decimals
    # Example:
    # 3.96 -> 0.0396
    df["spot_rate"] = (
        df["spot_rate"] / 100.0
    )

    validate_rate_column(
        df,
        "spot_rate"
    )

    spot_rates = {}

    for _, row in df.iterrows():

        term = float(row["t"])

        spot_rate = float(
            row["spot_rate"]
        )

        spot_rates[term] = spot_rate

    return YieldCurve(
        spot_rates
    )