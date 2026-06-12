import streamlit as st


def render_scenarios_section():

    st.header(
        "Scenarios"
    )

    scenario_file = st.file_uploader(
        "Scenario File",
        type=["csv"],
        key="scenario"
    )

    return scenario_file