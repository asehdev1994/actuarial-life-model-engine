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
        lapse=None,
        expenses=None
    ):

        self.mortality = mortality
        self.interest = interest
        self.lapse = lapse
        self.expenses_provider = expenses

    def qx(self, policy, age: int) -> float:

        return self.mortality.qx(policy, age)

    def px(self, policy, age: int) -> float:

        return self.mortality.px(policy, age)

    def discount_factor(self, t: float) -> float:

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
    
    def expenses(self, policy, t):
        """
        Return expense assumptions
        for a policy at time t.

        If no expense provider is supplied,
        default to zero expenses.
        """

        if self.expenses_provider is None:

            from model.assumptions.expense import (
                ExpenseResult
            )

            return ExpenseResult.zero()

        return self.expenses_provider.expenses(
            policy,
            t
        )