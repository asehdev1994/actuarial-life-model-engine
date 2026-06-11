from dataclasses import dataclass

@dataclass(frozen=True)
class StressDefinition:

    name: str

    target_assumption: str

    wrapper_factory: callable