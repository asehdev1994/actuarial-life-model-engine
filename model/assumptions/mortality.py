import numpy as np


class FormulaMortality:
    """
    Legacy formula-driven mortality provider.

    Retained temporarily while transitioning
    to table-driven mortality.
    """

    def qx(self, policy, age: int) -> float:

        q = 0.0005 * np.exp(0.08 * (age - 30))

        return min(q, 1.0)

    def px(self, policy, age: int) -> float:

        return 1 - self.qx(policy, age)


class MortalityTable:
    """
    Table-driven mortality provider.

    Responsible only for:
    - storing mortality rates
    - resolving qx(age)

    Does NOT:
    - read CSV files
    - perform interpolation
    - apply scenarios
    """

    def __init__(self, mortality_rates):

        self.mortality_rates = mortality_rates

    def qx(self, policy, age: int) -> float:
        """
        Return mortality rate for exact integer age.
        """

        if age not in self.mortality_rates:

            raise ValueError(
                f"No mortality rate found for age {age}"
            )

        return self.mortality_rates[age]

    def px(self, policy, age: int) -> float:

        return 1 - self.qx(policy, age)

    def __repr__(self):

        return (
            f"MortalityTable("
            f"ages={len(self.mortality_rates)}"
            f")"
        )