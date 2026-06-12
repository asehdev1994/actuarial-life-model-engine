import streamlit as st

from frontend.services.config_builder import (
    build_workflow_config
)

from frontend.services.workflow_runner import (
    execute_workflow
)


def render_execution_tab():

    st.header("Execution")

    if st.button(
        "Run Capital Workflow"
    ):

        uploaded_paths = (
            st.session_state[
                "uploaded_paths"
            ]
        )

        workflow_config = (
            build_workflow_config(
                uploaded_paths
            )
        )

        st.session_state[
            "workflow_config"
        ] = workflow_config

        workflow_result = (
            execute_workflow(
                workflow_config
            )
        )

        st.session_state[
            "workflow_result"
        ] = workflow_result

        st.success(
            "Workflow completed."
        )