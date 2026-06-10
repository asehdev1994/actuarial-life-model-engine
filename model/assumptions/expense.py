class ExpenseResult:
    """
    Structured expense output returned by the expense provider.

    Pure data container:
    - no projection logic
    - no valuation logic
    """

    def __init__(
        self,
        acquisition_expense: float = 0.0,
        maintenance_expense: float = 0.0
    ):

        self.acquisition_expense = acquisition_expense
        self.maintenance_expense = maintenance_expense

        self.total_expense = (
            acquisition_expense
            + maintenance_expense
        )

    @classmethod
    def zero(cls):

        return cls(
            acquisition_expense=0.0,
            maintenance_expense=0.0
        )

    def __repr__(self):

        return (
            f"ExpenseResult("
            f"acquisition_expense="
            f"{self.acquisition_expense:.2f}, "
            f"maintenance_expense="
            f"{self.maintenance_expense:.2f}, "
            f"total_expense="
            f"{self.total_expense:.2f}"
            f")"
        )
    
class ExpenseComponent:
    """
    Represents a single expense assumption component.

    Typically corresponds to one assumption row.

    Pure data container:
    - no projection logic
    - no valuation logic
    """

    def __init__(
        self,
        expense_type: str,
        amount_type: str,
        value: float,
        product_type: str = None
    ):

        self.expense_type = expense_type
        self.amount_type = amount_type
        self.value = value
        self.product_type = product_type

    def matches(self, policy, t: int) -> bool:
        """
        Determine whether this expense component
        applies to the policy and projection period.
        """

        if self.product_type is not None:

            if self.product_type != policy.product_type:

                return False

        return True

    def __repr__(self):

        return (
            f"ExpenseComponent("
            f"expense_type={self.expense_type}, "
            f"amount_type={self.amount_type}, "
            f"value={self.value}"
            f")"
        )
    
class ExpenseTable:
    """
    Provider of expense assumptions.

    Responsible for:
    - storing expense components
    - resolving applicable expenses
    - composing expense outputs

    Does NOT:
    - perform projection logic
    - perform valuation logic
    - read CSV files
    """

    def __init__(self, components):

        self.components = components

    def expense(self, policy, t: int) -> ExpenseResult:
        """
        Resolve expenses for a policy at time t.
        """

        result = ExpenseResult.zero()

        for component in self.components:

            if not component.matches(policy, t):

                continue

            expense_value = self._calculate_component_expense(
                component,
                policy,
                t
            )

            if component.expense_type == "acquisition":

                result.acquisition_expense += expense_value

            elif component.expense_type == "maintenance":

                result.maintenance_expense += expense_value

        result.total_expense = (
            result.acquisition_expense
            + result.maintenance_expense
        )

        return result
    
    def _calculate_component_expense(
        self,
        component,
        policy,
        t
    ) -> float:
        """
        Calculate raw expense amount
        for a single component.
        """

        if component.expense_type == "acquisition":

            if t > 0:

                return 0.0

        if component.amount_type == "fixed":

            return component.value

        elif component.amount_type == "premium_pct":

            return (
                component.value
                * policy.premium
            )

        raise ValueError(
            f"Unsupported amount_type: "
            f"{component.amount_type}"
        )