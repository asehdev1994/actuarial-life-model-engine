import streamlit as st

from frontend.components.portfolio_frontend import (
    render_portfolio_section
)

from frontend.components.assumptions_frontend import (
    render_assumptions_section
)

from frontend.components.scenarios_frontend import (
    render_scenarios_section
)

from frontend.components.correlations_frontend import (
    render_correlations_section
)

from frontend.services.file_storage import (
    persist_uploaded_file,
    persist_uploaded_files
)

from frontend.services.workflow_config_builder import (
    build_workflow_config
)

from frontend.services.workflow_runner import (
    execute_workflow
)


def render_inputs_tab():
    """
    Render workflow inputs and execute
    the actuarial model.
    """

    portfolio_file = (
        render_portfolio_section()
    )

    assumption_files = (
        render_assumptions_section()
    )

    scenario_file = (
        render_scenarios_section()
    )

    correlation_files = (
        render_correlations_section()
    )

    if st.button(
        "Run Model",
        key="run_model_button"
    ):

        portfolio_path = (
            persist_uploaded_file(
                portfolio_file
            )
        )

        assumption_paths = (
            persist_uploaded_files(
                assumption_files
            )
        )

        scenario_path = (
            persist_uploaded_file(
                scenario_file
            )
        )

        correlation_paths = (
            persist_uploaded_files(
                correlation_files
            )
        )

        workflow_config = (
            build_workflow_config(
                portfolio_path=(
                    portfolio_path
                ),

                assumption_paths=(
                    assumption_paths
                ),

                scenario_path=(
                    scenario_path
                ),

                correlation_paths=(
                    correlation_paths
                )
            )
        )

        result = (
            execute_workflow(
                workflow_config
            )
        )

        st.session_state[
            "result"
        ] = result

        st.success(
            "Model run completed. View results in the Results tab."
        )