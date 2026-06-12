import streamlit as st


def initialise_session_state():

    defaults = {
        "uploaded_paths": {},
        "workflow_config": None,
        "workflow_result": None
    }

    for key, value in defaults.items():

        if key not in st.session_state:

            st.session_state[key] = value