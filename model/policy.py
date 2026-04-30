# model/policy.py

class Policy:
    """
    Represents a single model point.

    In a real actuarial model, a portfolio would consist of many such policies,
    each with an associated weight.

    Basic policy attributes required for projection and valuation.
    
    """

    def __init__(
        self,
        age: int,
        term: int,
        sum_assured: float,
        premium: float,
        weight: int = 1
    ):
        self.age = age
        self.term = term
        self.sum_assured = sum_assured
        self.premium = premium
        self.weight = weight

    def __repr__(self):
        return (
            f"Policy(age={self.age}, term={self.term}, "
            f"sum_assured={self.sum_assured}, premium={self.premium}, "
            f"weight={self.weight})"
        )