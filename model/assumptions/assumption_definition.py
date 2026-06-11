from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class AssumptionDefinition:

    name: str

    config_attributes: list[str]

    loader: Callable

    null_provider_factory: Callable | None = None