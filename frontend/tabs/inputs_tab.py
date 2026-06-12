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

from frontend.services.user_config import (
    load_saved_inputs,
    save_inputs
)

from frontend.services.file_storage import (
    resolve_file_path
)

from pathlib import Path


def render_inputs_tab():
    """
    Render workflow inputs and execute
    the actuarial model.
    """

    saved_inputs = (
        load_saved_inputs()
    )

    portfolio_file = (
        render_portfolio_section()
    )

    portfolio_path = (
        saved_inputs.get(
            "portfolio_path"
        )
    )

    if portfolio_path:

        st.caption(
            f"✓ {Path(portfolio_path).name}"
        )

    assumption_files = (
        render_assumptions_section(
            saved_inputs.get(
                "assumption_paths",
                {}
            )
        )
    )

    scenario_file = (
        render_scenarios_section()
    )

    scenario_path = (
        saved_inputs.get(
            "scenario_path"
        )
    )

    if scenario_path:

        st.caption(
            f"✓ {Path(scenario_path).name}"
        )

    correlation_files = (
        render_correlations_section()
    )

    saved_correlations = (
        saved_inputs.get(
            "correlation_paths",
            {}
        )
    )

    for path in (
        saved_correlations.values()
    ):

        if path:

            st.caption(
                f"✓ {Path(path).name}"
            )

    if st.button(
        "Run Model",
        key="run_model_button"
    ):

        portfolio_path = (
            resolve_file_path(
                portfolio_file,
                saved_inputs.get(
                    "portfolio_path"
                )
            )
        )

        assumption_paths = {}

        for key, uploaded_file in (
            assumption_files.items()
        ):

            assumption_paths[
                key
            ] = resolve_file_path(
                uploaded_file,
                saved_inputs.get(
                    "assumption_paths",
                    {}
                ).get(key)
            )

        scenario_path = (
            resolve_file_path(
                scenario_file,
                saved_inputs.get(
                    "scenario_path"
                )
            )
        )

        correlation_paths = {}

        for key, uploaded_file in (
            correlation_files.items()
        ):

            correlation_paths[
                key
            ] = resolve_file_path(
                uploaded_file,
                saved_inputs.get(
                    "correlation_paths",
                    {}
                ).get(key)
            )

        save_inputs(
            {
                "portfolio_path":
                    portfolio_path,

                "assumption_paths":
                    assumption_paths,

                "scenario_path":
                    scenario_path,

                "correlation_paths":
                    correlation_paths
            }
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