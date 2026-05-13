import pandas as pd

def validate_required_columns(df, required_columns):
    """
    Validate that all required columns exist.
    """

    missing_columns = [
        column
        for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )
    
def validate_no_nulls(df, columns):
    """
    Validate that specified columns contain no null values.
    """

    null_columns = [
        column
        for column in columns
        if df[column].isnull().any()
    ]

    if null_columns:
        raise ValueError(
            f"Null values found in columns: {null_columns}"
        )
    
def validate_numeric_columns(df, columns):
    """
    Validate that specified columns contain numeric values.
    """

    invalid_columns = []

    for column in columns:

        converted = pd.to_numeric(
            df[column],
            errors="coerce"
        )

        if converted.isnull().any():
            invalid_columns.append(column)

    if invalid_columns:
        raise ValueError(
            f"Non-numeric values found in columns: {invalid_columns}"
        )
    
def validate_rate_column(df, column):
    """
    Validate that rate values are between 0 and 1.
    """

    invalid_rates = df[
        (df[column] < 0)
        | (df[column] > 1)
    ]

    if not invalid_rates.empty:
        raise ValueError(
            f"Invalid values found in '{column}'. "
            "Rates must be between 0 and 1."
        )
    
def validate_range_columns(df, start_col, end_col):
    """
    Validate that ranges are logically valid.
    """

    invalid_ranges = df[
        (df[start_col] < 0)
        | (df[end_col] < 0)
        | (df[start_col] > df[end_col])
    ]

    if not invalid_ranges.empty:
        raise ValueError(
            f"Invalid ranges found in "
            f"'{start_col}' and '{end_col}'."
        )
    
def validate_no_duplicate_segments(df, segment_columns):
    """
    Validate that no duplicate assumption segments exist.
    """

    duplicates = df[
        df.duplicated(
            subset=segment_columns,
            keep=False
        )
    ]

    if not duplicates.empty:
        raise ValueError(
            "Duplicate assumption segments found."
        )
    
def validate_no_overlapping_ranges(
    df,
    segment_columns,
    start_col,
    end_col
):
    """
    Validate that segmented ranges do not overlap.
    """

    grouped = df.groupby(segment_columns)

    for group_key, group_df in grouped:

        sorted_group = group_df.sort_values(start_col)

        rows = sorted_group.to_dict("records")

        for i in range(len(rows) - 1):

            current_row = rows[i]
            next_row = rows[i + 1]

            current_end = current_row[end_col]
            next_start = next_row[start_col]

            if next_start <= current_end:

                raise ValueError(
                    f"Overlapping ranges detected for "
                    f"segment {group_key}."
                )
            
def validate_non_negative_column(df, column):
    """
    Validate that a numeric column contains
    no negative values.
    """

    invalid = df[df[column] < 0]

    if not invalid.empty:

        raise ValueError(
            f"Negative values found in '{column}'."
        )