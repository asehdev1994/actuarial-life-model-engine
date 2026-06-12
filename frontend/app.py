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

from components.assumptions_frontend import (
    render_assumptions_section
)

st.title(
    "Actuarial Life Model Engine"
)

uploaded_files = (
    render_assumptions_section()
)

st.divider()

st.subheader(
    "Debug Output"
)

st.write(
    list(uploaded_files.keys())
)