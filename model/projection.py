# model/projection.py

def project_cashflows(policy, assumptions):
    """
    Project expected cashflows for a single policy.
    """

    results = []
    prob_alive = 1.0

    for t in range(policy.term):
        age_t = policy.age + t

        q = assumptions.qx(age_t)

        expected_premium = policy.premium * prob_alive
        expected_claim = policy.sum_assured * prob_alive * q

        results.append({
            "t": t,
            "age": age_t,
            "prob_alive": prob_alive,
            "qx": q,
            "expected_premium": expected_premium,
            "expected_claim": expected_claim
        })

        prob_alive *= (1 - q)

    return results