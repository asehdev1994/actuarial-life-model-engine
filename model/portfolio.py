from model.valuation import value_policy


def value_portfolio(policies, assumptions):
    """
    Calculate the aggregated present value of a portfolio of policies.

    Parameters:
    policies (list): List of Policy objects
    assumptions (Assumptions): Assumptions object

    Returns:
    dict: Aggregated valuation results
    """

    pv_premiums = 0.0
    pv_claims = 0.0

    # Handle empty portfolio explicitly
    if not policies:
        return {
            "pv_premiums": 0.0,
            "pv_claims": 0.0,
            "net_value": 0.0
        }

    for policy in policies:
        result = value_policy(policy, assumptions)

        weight = policy.weight

        pv_premiums += result.pv_premiums * weight
        pv_claims += result.pv_claims * weight

    net_value = pv_premiums - pv_claims

    return {
        "pv_premiums": pv_premiums,
        "pv_claims": pv_claims,
        "net_value": net_value
    }