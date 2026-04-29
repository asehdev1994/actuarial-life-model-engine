import pandas as pd


def build_profit_dataframe(result):
    """
    Convert valuation breakdown into a clean DataFrame.
    """

    return pd.DataFrame(result["breakdown"])


def add_profit_signature(df):
    """
    Add profit signature metrics.
    """

    total_profit = df["pv_net"].sum()

    df = df.copy()

    df["profit_pct"] = df["pv_net"] / total_profit

    return df


def summary_metrics(df):
    """
    Return key summary statistics.
    """

    return {
        "total_pv_profit": df["pv_net"].sum(),
        "total_cash_profit": df["net_cashflow"].sum(),
        "peak_profit_year": df.loc[df["pv_net"].idxmax(), "t"]
    }