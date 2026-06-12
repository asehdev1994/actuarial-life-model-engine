import tempfile
from pathlib import Path


TEMP_DIR = Path(
    tempfile.gettempdir()
) / "actuarial_model_uploads"

TEMP_DIR.mkdir(
    exist_ok=True
)


def save_uploaded_file(uploaded_file):

    if uploaded_file is None:
        return None

    file_path = (
        TEMP_DIR / uploaded_file.name
    )

    with open(file_path, "wb") as f:

        f.write(
            uploaded_file.getbuffer()
        )

    return str(file_path)