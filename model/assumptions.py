import numpy as np


class Assumptions:
    """
    Central place for all model assumptions.

    This includes:
    - Mortality (qx)
    - Survival (px)
    - Interest rates / discounting
    """

    def __init__(self, interest_rate=0.03):
        """
        Initialise assumptions.

        Parameters:
        interest_rate (float): Annual discount rate
        """
        self.interest_rate = interest_rate

    def qx(self, age: int) -> float:
        """
        qx is the probability of death within one year.

        This synthetic curve is used for demonstration purposes only.
        - Low at young ages
        - Increases exponentially with age

        In production models, this would be derived from mortality tables (planned future update).

        """

        q = 0.0005 * np.exp(0.08 * (age - 30))

        # Ensure probability never exceeds 1
        return min(q, 1.0)

    def px(self, age: int) -> float:
        """
        px is the probability of survival over one year.
        Defined as 1 - qx, assuming no other decrements.

        """
        return 1 - self.qx(age)

    def discount_factor(self, t: int) -> float:
        """
        Standard discrete discounting.
        Assumes a flat interest rate across all durations (planned future update).

        """

        return 1 / ((1 + self.interest_rate) ** t)