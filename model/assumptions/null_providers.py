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