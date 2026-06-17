from pathlib import Path


def save_uploaded_file(
    uploaded_file
):
    """
    Persist a Streamlit UploadedFile
    to a project directory.

    Returns:
        str: path to saved file
    """

    upload_dir = (
        Path(__file__)
        .parent.parent
        / "temp_uploads"
    )

    upload_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    destination = (
        upload_dir
        / uploaded_file.name
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

def resolve_file_path(
    uploaded_file,
    existing_path=None
):
    """
    Use uploaded file if supplied.

    Otherwise use existing saved path.
    """

    if uploaded_file is not None:

        return save_uploaded_file(
            uploaded_file
        )

    return existing_path