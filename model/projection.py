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
    prob_alive = 1.0

    for t in range(policy.term):
        age_t = policy.age + t

        # Probability of death at age t
        q = assumptions.qx(age_t)

        # Premium is received only if the policyholder is alive
        # → weighted by probability of survival
        expected_premium = policy.premium * prob_alive

        # Claim occurs if the policyholder dies during the year
        # → probability = prob_alive * qx
        expected_claim = policy.sum_assured * prob_alive * q

        results.append(
            ProjectionRow(
                t=t,
                age=age_t,
                prob_alive=prob_alive,
                qx=q,
                expected_premium=expected_premium,
                expected_claim=expected_claim
            )
        )

        # Update survival probability for next period
        prob_alive *= (1 - q)

    return ProjectionResult(rows=results)