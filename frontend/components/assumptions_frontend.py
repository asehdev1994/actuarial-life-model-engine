import streamlit as st

from model.assumptions.assumption_registry import (
    ASSUMPTION_REGISTRY
)

def build_upload_label(
    attribute_name: str
) -> str:

    return (
        attribute_name
        .replace("_path", "")
        .replace("_", " ")
        .title()
    )

def render_assumptions_section():
    st.header(
        "Assumptions"
    )

    uploaded_files = {}

    for definition in ASSUMPTION_REGISTRY.values():
        
        st.subheader(
            definition.display_name
        )

        if definition.description:

            st.caption(
                definition.description
            )
        
        for attribute in (
            definition.config_attributes
        ):
            label = build_upload_label(
                attribute
            )

            uploaded_file = st.file_uploader(
                label,
                key=attribute
            )

            uploaded_files[
                attribute
            ] = uploaded_file

    return uploaded_files