import streamlit as st


def render_portfolio_section():

    st.header(
        "Portfolio"
    )

    portfolio_file = st.file_uploader(
        "Portfolio CSV",
        type=["csv"],
        key="portfolio"
    )

    return portfolio_file