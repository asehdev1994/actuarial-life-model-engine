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
        Probability of death between age x and x+1.

        We use a synthetic mortality curve:
        - Low at young ages
        - Increases exponentially with age
        """

        q = 0.0005 * np.exp(0.08 * (age - 30))

        # Ensure probability never exceeds 1
        return min(q, 1.0)

    def px(self, age: int) -> float:
        """
        Probability of survival over one year.
        """
        return 1 - self.qx(age)

    def discount_factor(self, t: int) -> float:
        """
        Discount factor for time t.
        """

        return 1 / ((1 + self.interest_rate) ** t)