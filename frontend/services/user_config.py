import json
from pathlib import Path


CONFIG_PATH = (
    Path(__file__).parent.parent
    / "config"
    / "last_run.json"
)


def load_saved_inputs():

    if not CONFIG_PATH.exists():

        return {}

    with open(
        CONFIG_PATH,
        "r"
    ) as file:

        return json.load(
            file
        )


def save_inputs(
    data
):

    CONFIG_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        CONFIG_PATH,
        "w"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )