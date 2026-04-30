# model/valuation.py

from model.projection import project_cashflows
from model.results import ValuationResult


def value_policy(policy, assumptions, return_breakdown=False):
    """
    Calculate present value of a single policy.

    Steps:
    1. Project expected cashflows
    2. Apply discounting
    3. Aggregate PV premiums and claims
    4. (Optional) build detailed breakdown for analysis

    """

    projection = project_cashflows(policy, assumptions)

    pv_premiums = 0.0
    pv_claims = 0.0

    breakdown = []

    for row in projection:
        t = row["t"]
        
        # Apply discount factor to convert future cashflows to present value
        discount = assumptions.discount_factor(t)

        pv_premium_t = row["expected_premium"] * discount
        pv_claim_t = row["expected_claim"] * discount

        # Net cashflow before discounting
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

    # Build breakdown
    # Build cumulative profit and cashflow over time
    # This is used for profit emergence analysis
    if return_breakdown:
        cum_profit = 0.0
        cum_cashflow = 0.0
        for row in breakdown:
            cum_profit += row["pv_net"]
            cum_cashflow += row["net_cashflow"]

            row["cum_profit"] = cum_profit
            row["cum_cashflow"] = cum_cashflow
    else:
        breakdown = None


    # Return structured valuation output
    return ValuationResult(
        pv_premiums=pv_premiums,
        pv_claims=pv_claims,
        net_value=net_value,
        breakdown=breakdown
    )