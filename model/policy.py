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
        gender: str = "M",
        smoker_status: str = "Non-Smoker",
        product_type: str = "Term",
        weight: int = 1
    ):
        self.age = age
        self.term = term
        self.sum_assured = sum_assured
        self.premium = premium
        self.gender = gender
        self.smoker_status = smoker_status
        self.product_type = product_type
        self.weight = weight

    def __repr__(self):
        return (
            f"Policy(age={self.age}, term={self.term}, "
            f"sum_assured={self.sum_assured}, premium={self.premium}, "
            f"gender={self.gender}, "
            f"smoker_status={self.smoker_status}, "
            f"product_type={self.product_type}, "
            f"weight={self.weight})"
        )