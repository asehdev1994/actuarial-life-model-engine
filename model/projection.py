# model/projection.py

from model.results import ProjectionRow, ProjectionResult

def project_cashflows(policy, assumptions):
    """
    Project expected cashflows for a single policy.

    Key approach:
    - Uses unconditional probabilities (not path simulation)
    - Tracks probability of survival over time
    - Calculates expected values of premiums and claims
    
    """

    results = []

    # Probability that the policyholder is alive at time t.
    # Starts at 1 and evolves over time using survival probabilities.
    prob_inforce = 1.0

    for t in range(policy.term):
        age_t = policy.age + t

        # Probability of death at age t
        q = assumptions.qx(policy, age_t)
        lapse_rate = assumptions.lapse_rate(policy, t)

        # Premium is received only if the policyholder is alive
        # → weighted by probability of survival
        expected_premium = policy.premium * prob_inforce

        # Claim occurs if the policyholder dies during the year
        # → probability = prob_inforce * qx
        expected_claim = policy.sum_assured * prob_inforce * q
        expected_lapse = prob_inforce * lapse_rate

        results.append(
            ProjectionRow(
                t=t,
                age=age_t,
                prob_inforce=prob_inforce,
                qx=q,
                lapse_rate=lapse_rate,
                expected_premium=expected_premium,
                expected_claim=expected_claim,
                expected_lapse=expected_lapse
            )
        )

        # Update survival probability for next period
        prob_inforce *= (1 - q - lapse_rate)

    return ProjectionResult(rows=results)