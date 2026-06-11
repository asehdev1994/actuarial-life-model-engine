class AssumptionConfig:
    """
    Centralised assumption ingestion configuration.

    Responsibilities:
    - own assumption file paths
    - centralise workflow assumption inputs
    - support scalable assumption expansion

    Does NOT:
    - load assumptions
    - perform validation
    - construct providers
    """

    def __init__(
        self,
        values: dict[str, str | None]
    ):

        self.values = values

    def __getattr__(self, name):

        if name in self.values:

            return self.values[name]

        raise AttributeError(name)

    def __repr__(self):

        return (
            f"AssumptionConfig("
            f"values={self.values}"
            f")"
        )