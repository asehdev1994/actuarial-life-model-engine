class CapitalWorkflowConfig:
    """
    Unified capital workflow execution configuration.

    Responsibilities:
    - centralise workflow execution inputs
    - compose workflow configuration objects
    - support future frontend integration

    Does NOT:
    - execute workflow logic
    - load files
    - perform calculations
    """

    def __init__(
        self,
        portfolio_path,
        scenario_path,
        assumption_config,
        correlation_config,
        return_breakdown=False
    ):

        self.portfolio_path = (
            portfolio_path
        )

        self.scenario_path = (
            scenario_path
        )

        self.assumption_config = (
            assumption_config
        )

        self.correlation_config = (
            correlation_config
        )

        self.return_breakdown = (
            return_breakdown
        )

    def __repr__(self):

        return (
            f"CapitalWorkflowConfig("
            f"portfolio_path="
            f"{self.portfolio_path}, "
            f"scenario_path="
            f"{self.scenario_path}"
            f")"
        )