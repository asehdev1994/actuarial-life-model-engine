from pathlib import Path
import tempfile


def save_uploaded_file(
    uploaded_file
):
    """
    Persist a Streamlit UploadedFile
    to a temporary file.

    Returns:
        str: path to saved file
    """

    temp_dir = Path(
        tempfile.gettempdir()
    )

    destination = (
        temp_dir /
        uploaded_file.name
    )

    destination.write_bytes(
        uploaded_file.getbuffer()
    )

    return str(
        destination
    )


def persist_uploaded_files(
    uploaded_files
):
    """
    Persist a dictionary of uploaded files.

    Input:

    {
        "mortality_table_path":
            UploadedFile(...),

        "yield_curve_path":
            UploadedFile(...)
    }

    Output:

    {
        "mortality_table_path":
            "/tmp/ons_mortality.csv",

        "yield_curve_path":
            "/tmp/sonia_spot_rates.csv"
    }
    """

    saved_paths = {}

    for (
        key,
        uploaded_file
    ) in uploaded_files.items():

        if uploaded_file is None:

            saved_paths[
                key
            ] = None

            continue

        saved_paths[
            key
        ] = save_uploaded_file(
            uploaded_file
        )

    return saved_paths

def persist_uploaded_file(
    uploaded_file
):
    """
    Persist a single uploaded file.

    Returns:
        str | None
    """

    if uploaded_file is None:

        return None

    return save_uploaded_file(
        uploaded_file
    )