import streamlit as st

from model.assumptions.assumption_registry import (
    ASSUMPTION_REGISTRY
)

from pathlib import Path

def build_upload_label(
    attribute_name: str
) -> str:

    return (
        attribute_name
        .replace("_path", "")
        .replace("_", " ")
        .title()
    )

def render_assumptions_section(
        existing_paths=None
):
    
    if existing_paths is None:

        existing_paths = {}

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

            saved_path = (
                existing_paths.get(
                    attribute
                )
            )

            if saved_path:

                st.caption(
                    f"✓ {Path(saved_path).name}"
                )

            uploaded_file = st.file_uploader(
                label,
                key=attribute
            )

            uploaded_files[
                attribute
            ] = uploaded_file

    return uploaded_files