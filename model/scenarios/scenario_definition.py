class ScenarioDefinition:
    """
    Defines a scenario overlay applied to assumptions.

    Pure data container:
    - no projection logic
    - no valuation logic
    - no stressing mechanics

    Responsibilities:
    - define stress parameters
    - provide stable scenario metadata

    Scenario application is delegated elsewhere.
    """

    def __init__(
        self,
        scenario_id: str,
        name: str,
        risk_type: str,
        mortality_multiplier: float = 1.0,
        lapse_multiplier: float = 1.0,
        interest_rate_shift: float = 0.0,
        expense_multiplier: float = 1.0
    ):

        self.scenario_id = scenario_id
        self.risk_type = risk_type
        self.name = name

        self.mortality_multiplier = (
            mortality_multiplier
        )

        self.lapse_multiplier = (
            lapse_multiplier
        )

        self.interest_rate_shift = (
            interest_rate_shift
        )

        self.expense_multiplier = (
            expense_multiplier
        )

    def __repr__(self):

        return (
            f"ScenarioDefinition("
            f"scenario_id={self.scenario_id}, "
            f"risk_type={self.risk_type}, "
            f"name={self.name}, "
            f"mortality_multiplier="
            f"{self.mortality_multiplier}, "
            f"lapse_multiplier="
            f"{self.lapse_multiplier}, "
            f"interest_rate_shift="
            f"{self.interest_rate_shift}, "
            f"expense_multiplier="
            f"{self.expense_multiplier}"
            f")"
        )