class AssumptionSet:
    """
    Unified assumptions interface consumed by the engine.

    Projection and valuation should depend only on this interface,
    not on specific assumption implementations.
    """

    def __init__(
        self,
        mortality,
        interest
    ):

        self.mortality = mortality
        self.interest = interest

    def qx(self, age: int) -> float:

        return self.mortality.qx(age)

    def px(self, age: int) -> float:

        return self.mortality.px(age)

    def discount_factor(self, t: int) -> float:

        return self.interest.discount_factor(t)