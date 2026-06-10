class AssumptionSet:
    """
    Unified assumptions interface consumed by the engine.

    Projection and valuation should depend only on this interface,
    not on specific assumption implementations.
    """

    def __init__(
        self,
        providers
    ):
                self.providers = providers
        
    @property
    def mortality(self):
        return self.providers["mortality"]
    
    @property
    def interest(self):
        return self.providers["interest"]
    
    @property
    def lapse(self):
        return self.providers.get("lapse")
    
    @property
    def expense(self):
        return self.providers.get("expense")

    def qx(self, policy, age: int) -> float:

        return self.mortality.qx(policy, age)

    def px(self, policy, age: int) -> float:

        return self.mortality.px(policy, age)

    def discount_factor(self, t: float) -> float:

        return self.interest.discount_factor(t)
    
    def lapse_rate(self, policy, t: int) -> float:

        return self.lapse.lapse_rate(policy, t)
    
    def expense_result(self, policy, t):
        
        return self.expense.expense(
            policy,
            t
        )