from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class AssumptionDefinition:

    name: str

    display_name: str

    config_attributes: list[str]

    loader: Callable

    description: str | None = None

    null_provider_factory: Callable | None = None