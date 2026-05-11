from model.valuation import value_policy
from model.results import PortfolioResult


class Portfolio:
    """
    Represents a portfolio of insurance policies.

    Responsibilities:
    - store policies
    - aggregate valuation results

    No projection or actuarial mechanics belong here.
    """

    def __init__(self, policies):

        self.policies = policies

    def value(self, assumptions):
        """
        Calculate aggregated portfolio valuation.
        """

        pv_premiums = 0.0
        pv_claims = 0.0

        # Handle empty portfolio explicitly
        if not self.policies:

            return PortfolioResult(
                pv_premiums=0.0,
                pv_claims=0.0,
                net_value=0.0,
                policy_count=0
            )

        for policy in self.policies:

            result = value_policy(policy, assumptions)

            weight = policy.weight

            pv_premiums += result.pv_premiums * weight
            pv_claims += result.pv_claims * weight

        net_value = pv_premiums - pv_claims

        return PortfolioResult(
            pv_premiums=pv_premiums,
            pv_claims=pv_claims,
            net_value=net_value,
            policy_count=len(self.policies)
        )