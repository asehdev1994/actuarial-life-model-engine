import numpy as np


class MortalityTable:
    """
    Mortality assumption provider.

    Responsible only for:
    - qx
    - px

    No discounting or lapse behaviour belongs here.
    """

    def qx(self, age: int) -> float:
        """
        Probability of death within one year.
        """

        q = 0.0005 * np.exp(0.08 * (age - 30))

        return min(q, 1.0)

    def px(self, age: int) -> float:
        """
        One-year survival probability.
        """

        return 1 - self.qx(age)