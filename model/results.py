# model/results.py

from typing import List, Dict, Optional


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