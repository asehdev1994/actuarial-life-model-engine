class FlatYieldCurve:
    """
    Simple flat interest rate provider.

    Retained for backward compatibility
    and simple deterministic testing.
    """

    def __init__(self, interest_rate=0.03):

        self.interest_rate = interest_rate

    def discount_factor(self, t: float) -> float:
        """
        Standard discrete discounting.
        """

        return 1 / ((1 + self.interest_rate) ** t)


class YieldCurve:
    """
    Table-driven yield curve provider.

    Responsible only for:
    - storing spot rates
    - resolving discount factors
    - handling terminal extrapolation

    Does NOT:
    - read CSV files
    - interpolate rates
    - perform scenario modelling
    """

    def __init__(self, spot_rates):

        self.spot_rates = spot_rates

        self.max_term = max(
            self.spot_rates.keys()
        )

    def _resolve_rate(self, t: float) -> float:
        """
        Resolve spot rate for maturity t.

        Version 1 behaviour:
        - exact maturity lookup
        - terminal extrapolation beyond max term
        """

        # Time-0 discounting
        # DF(0) is always 1 by definition
        if t == 0:

            return 0.0

        # Terminal extrapolation
        if t > self.max_term:

            return self.spot_rates[
                self.max_term
            ]

        if t not in self.spot_rates:

            raise ValueError(
                f"No spot rate found for "
                f"term={t}"
            )

        return self.spot_rates[t]

    def discount_factor(self, t: float) -> float:
        """
        Calculate discount factor
        using spot discounting.
        """

        rate = self._resolve_rate(t)

        return 1 / ((1 + rate) ** t)

    def __repr__(self):

        return (
            f"YieldCurve("
            f"terms={len(self.spot_rates)}, "
            f"max_term={self.max_term}"
            f")"
        )