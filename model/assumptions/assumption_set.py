class AssumptionSet:
    """
    Unified assumptions interface consumed by the engine.

    Projection and valuation should depend only on this interface,
    not on specific assumption implementations.
    """

    def __init__(
        self,
        mortality,
        interest,
        lapse=None
    ):

        self.mortality = mortality
        self.interest = interest
        self.lapse = lapse

    def qx(self, policy, age: int) -> float:

        return self.mortality.qx(policy, age)

    def px(self, policy, age: int) -> float:

        return self.mortality.px(policy, age)

    def discount_factor(self, t: int) -> float:

        return self.interest.discount_factor(t)
    
    def lapse_rate(self, policy, t: int) -> float:
        """
        Return lapse rate for a policy at time t.

        If no lapse assumptions are supplied,
        default to zero lapse.
        """

        if self.lapse is None:

            return 0.0

        return self.lapse.lapse_rate(policy, t)