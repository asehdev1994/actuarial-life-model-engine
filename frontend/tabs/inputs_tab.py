import streamlit as st

from frontend.services.temp_storage import (
    save_uploaded_file
)


def render_inputs_tab():

    st.header("Model Inputs")

    upload_fields = {
        "mortality_table":
            "Mortality Table CSV",

        "mortality_parameters":
            "Mortality Parameters CSV",

        "yield_curve":
            "Yield Curve CSV",

        "lapse_table":
            "Lapse Table CSV",

        "expense_table":
            "Expense Table CSV",

        "scenario_csv":
            "Scenario CSV",

        "life_correlation":
            "Life Correlation Matrix CSV",

        "market_correlation":
            "Market Correlation Matrix CSV",

        "bscr_correlation":
            "BSCR Correlation Matrix CSV",

        "portfolio":
            "Portfolio CSV"
    }

    uploaded_paths = {}

    for key, label in upload_fields.items():

        uploaded_file = st.file_uploader(
            label,
            type="csv",
            key=key
        )

        if uploaded_file is not None:

            uploaded_paths[key] = (
                save_uploaded_file(
                    uploaded_file
                )
            )

    st.session_state[
        "uploaded_paths"
    ] = uploaded_paths

    if uploaded_paths:

        st.success(
            "Files uploaded successfully."
        )