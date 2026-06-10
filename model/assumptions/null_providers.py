class NullLapseProvider:

    def lapse_rate(
        self,
        policy,
        t
    ):
        return 0.0
    
class NullExpenseProvider:

    def expense(
        self,
        policy,
        t
    ):
        from model.assumptions.expense import (
            ExpenseResult
        )

        return ExpenseResult.zero()
    
class NullMortalityProvider:

    def qx(self, policy, age):
        return 0.0

    def px(self, policy, age):
        return 1.0
    
class NullInterestProvider:

    def discount_factor(self, t):
        return 1.0