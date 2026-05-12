import pandas as pd

from model.assumptions.lapse import (
    LapseSegment,
    LapseTable
)

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