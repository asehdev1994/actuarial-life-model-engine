import streamlit as st


def render_base_metrics(
    workflow_result
):

    st.subheader(
        "Base Results"
    )

    st.metric(
        "Base BEL",
        round(
            workflow_result.base_bel,
            2
        )
    )