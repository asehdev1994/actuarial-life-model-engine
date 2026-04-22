# model/policy.py

class Policy:
    """
    Represents a single life insurance policy (model point).

    This class is a pure data container and should not contain
    any projection or actuarial logic.
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