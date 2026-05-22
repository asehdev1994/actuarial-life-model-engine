import streamlit as st

from frontend.rendering.metrics import (
    render_base_metrics
)

from frontend.rendering.scr_tables import (
    render_scr_table
)


def render_results_tab():

    st.header("Results")

    workflow_result = (
        st.session_state[
            "workflow_result"
        ]
    )

    if workflow_result is None:

        st.info(
            "No workflow results available."
        )

        return

    render_base_metrics(
        workflow_result
    )

    render_scr_table(
        workflow_result
    )