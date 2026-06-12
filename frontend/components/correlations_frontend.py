import streamlit as st


def render_correlations_section():

    st.header(
        "Correlations"
    )

    life_file = st.file_uploader(
        "Life Correlation Matrix",
        type=["csv"],
        key="life_correlation"
    )

    market_file = st.file_uploader(
        "Market Correlation Matrix",
        type=["csv"],
        key="market_correlation"
    )

    bscr_file = st.file_uploader(
        "BSCR Correlation Matrix",
        type=["csv"],
        key="bscr_correlation"
    )

    return {
        "life": life_file,
        "market": market_file,
        "bscr": bscr_file
    }