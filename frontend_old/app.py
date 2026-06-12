import sys
from pathlib import Path

PROJECT_ROOT = (
    Path(__file__).resolve().parents[1]
)

sys.path.append(
    str(PROJECT_ROOT)
)

import streamlit as st

from frontend.state.session_state import (
    initialise_session_state
)

from frontend.tabs.inputs_tab import (
    render_inputs_tab
)

from frontend.tabs.execution_tab import (
    render_execution_tab
)

from frontend.tabs.results_tab import (
    render_results_tab
)


st.set_page_config(
    page_title="Actuarial Capital Engine",
    layout="wide"
)

initialise_session_state()

st.title(
    "Actuarial Life Model Engine"
)

inputs_tab, execution_tab, results_tab = (
    st.tabs([
        "Inputs",
        "Execution",
        "Results"
    ])
)

with inputs_tab:

    render_inputs_tab()

with execution_tab:

    render_execution_tab()

with results_tab:

    render_results_tab()