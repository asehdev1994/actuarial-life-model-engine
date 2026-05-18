class StressedMortalityTable:
    """
    Mortality provider wrapper applying
    scenario-based mortality stresses.

    Responsibilities:
    - wrap an existing mortality provider
    - apply mortality stress overlays
    - preserve mortality provider interface

    Does NOT:
    - perform projection logic
    - perform valuation logic
    - know SCR calculations
    """

    def __init__(
        self,
        base_mortality,
        mortality_multiplier: float = 1.0
    ):

        self.base_mortality = base_mortality

        self.mortality_multiplier = (
            mortality_multiplier
        )

    def qx(self, policy, age: int) -> float:
        """
        Resolve stressed mortality.
        """

        base_qx = self.base_mortality.qx(
            policy,
            age
        )

        stressed_qx = (
            base_qx
            * self.mortality_multiplier
        )

        return min(stressed_qx, 1.0)

    def px(self, policy, age: int) -> float:

        return 1 - self.qx(policy, age)

    def __repr__(self):

        return (
            f"StressedMortalityTable("
            f"multiplier="
            f"{self.mortality_multiplier}"
            f")"
        )