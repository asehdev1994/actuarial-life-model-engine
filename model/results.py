# model/results.py

from typing import List, Dict, Optional

class ProjectionRow:
    """
    Represents one projected time period.

    Pure data container:
    - no projection logic
    - no actuarial calculations

    Used as the structured output of projection.py
    """

    __slots__ = [
        "t",
        "age",
        "prob_alive",
        "qx",
        "expected_premium",
        "expected_claim"
    ]

    def __init__(
        self,
        t: int,
        age: int,
        prob_alive: float,
        qx: float,
        expected_premium: float,
        expected_claim: float
    ):

        self.t = t
        self.age = age
        self.prob_alive = prob_alive
        self.qx = qx
        self.expected_premium = expected_premium
        self.expected_claim = expected_claim

    def to_dict(self) -> dict:
        """
        Convert to dictionary for compatibility/debugging.
        """

        return {
            "t": self.t,
            "age": self.age,
            "prob_alive": self.prob_alive,
            "qx": self.qx,
            "expected_premium": self.expected_premium,
            "expected_claim": self.expected_claim
        }

    def __repr__(self):

        return (
            f"ProjectionRow("
            f"t={self.t}, "
            f"age={self.age}, "
            f"prob_alive={self.prob_alive:.6f}, "
            f"qx={self.qx:.6f}"
            f")"
        )

class ProjectionResult:
    """
    Container for projected policy cashflows.

    Holds all projection rows produced during projection.

    Design:
    - structured output contract
    - no actuarial logic
    """

    __slots__ = ["rows"]

    def __init__(self, rows: List[ProjectionRow]):

        if not isinstance(rows, list):
            raise TypeError("rows must be a list")

        self.rows = rows

    def to_dict(self) -> dict:
        """
        Convert projection rows into serialisable format.
        """

        return {
            "rows": [row.to_dict() for row in self.rows]
        }

    def __repr__(self):

        return (
            f"ProjectionResult("
            f"rows={len(self.rows)}"
            f")"
        )

class ValuationResult:
    """
    Structured output of a policy valuation.

    Fields:
    - pv_premiums: Present value of premiums
    - pv_claims: Present value of claims
    - net_value: Net present value
    - breakdown: Optional per-period results

    Design:
    - Pure data container
    - No actuarial or analytical logic

    Acts as the contract between valuation and analysis layers

    """

    __slots__ = ["pv_premiums", "pv_claims", "net_value", "breakdown"]

    def __init__(
        self,
        pv_premiums: float,
        pv_claims: float,
        net_value: float,
        breakdown: Optional[List[Dict]] = None
    ):
        # Basic validation (lightweight, no behaviour change)
        if breakdown is not None and not isinstance(breakdown, list):
            raise TypeError("breakdown must be a list of dictionaries or None")

        # Explicit typing (contract clarity)
        self.pv_premiums: float = pv_premiums
        self.pv_claims: float = pv_claims
        self.net_value: float = net_value
        self.breakdown: Optional[List[Dict]] = breakdown

    # Provided for backward compatibility and easy serialisation
    def to_dict(self) -> dict:
        """
        Convert to dictionary (for backward compatibility).
        """
        result = {
            "pv_premiums": self.pv_premiums,
            "pv_claims": self.pv_claims,
            "net_value": self.net_value
        }

        if self.breakdown is not None:
            result["breakdown"] = self.breakdown

        return result

    def __repr__(self):
        return (
            f"ValuationResult("
            f"pv_premiums={self.pv_premiums:.2f}, "
            f"pv_claims={self.pv_claims:.2f}, "
            f"net_value={self.net_value:.2f}, "
            f"breakdown={'Yes' if self.breakdown else 'No'}"
            f")"
        )