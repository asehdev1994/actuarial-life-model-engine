# model/valuation.py

from model.projection import project_cashflows


def value_policy(policy, assumptions, return_breakdown=False):
    """
    Calculate present value of a single policy.

    Parameters:
    policy: Policy object
    assumptions: Assumptions object
    return_breakdown (bool): whether to return per-period results

    Returns:
    Dictionary containing valuation results
    """

    projection = project_cashflows(policy, assumptions)

    pv_premiums = 0.0
    pv_claims = 0.0

    breakdown = []

    for row in projection:
        t = row["t"]
        discount = assumptions.discount_factor(t)

        pv_premium_t = row["expected_premium"] * discount
        pv_claim_t = row["expected_claim"] * discount
        net_cf_t = row["expected_premium"] - row["expected_claim"]
        pv_net_t = pv_premium_t - pv_claim_t

        pv_premiums += pv_premium_t
        pv_claims += pv_claim_t

        if return_breakdown:
            breakdown.append({
                "t": t,
                "age": row["age"],
                "discount_factor": discount,
                "expected_premium": row["expected_premium"],
                "expected_claim": row["expected_claim"],
                "net_cashflow": net_cf_t,
                "pv_premium": pv_premium_t,
                "pv_claim": pv_claim_t,
                "pv_net": pv_net_t
            })

    net_value = pv_premiums - pv_claims

    result = {
        "pv_premiums": pv_premiums,
        "pv_claims": pv_claims,
        "net_value": net_value
    }

    if return_breakdown:
        cum_profit = 0.0
        cum_cashflow = 0.0
        for row in breakdown:
            cum_profit += row["pv_net"]
            cum_cashflow += row["net_cashflow"]

            row["cum_profit"] = cum_profit
            row["cum_cashflow"] = cum_cashflow

        result["breakdown"] = breakdown

    return result