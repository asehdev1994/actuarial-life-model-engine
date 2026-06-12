import os
import sys

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

import streamlit as st

from frontend.tabs.inputs_tab import (
    render_inputs_tab
)

from frontend.tabs.results_tab import (
    render_results_tab
)

st.title(
    "Actuarial Life Model Engine"
)

inputs_tab, results_tab = st.tabs(
    [
        "Inputs",
        "Results"
    ]
)

with inputs_tab:

    render_inputs_tab()

with results_tab:

    render_results_tab(
        st.session_state.get(
            "result"
        )
    )