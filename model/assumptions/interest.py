class FlatYieldCurve:
    """
    Interest rate assumption provider.

    Responsible only for discounting.
    """

    def __init__(self, interest_rate=0.03):

        self.interest_rate = interest_rate

    def discount_factor(self, t: int) -> float:
        """
        Standard discrete discounting.
        """

        return 1 / ((1 + self.interest_rate) ** t)