import numpy as np


class FormulaMortality:
    """
    Legacy formula-driven mortality provider.

    Retained temporarily while transitioning
    to table-driven mortality.
    """

    def qx(self, policy, age: int) -> float:

        q = 0.0005 * np.exp(0.08 * (age - 30))

        return min(q, 1.0)

    def px(self, policy, age: int) -> float:

        return 1 - self.qx(policy, age)


class MortalityTable:
    """
    Table-driven mortality provider.

    Responsible only for:
    - storing mortality rates
    - resolving qx(age)

    Does NOT:
    - read CSV files
    - perform interpolation
    - apply scenarios
    """

    def __init__(
            self, 
            mortality_rates,
            mortality_parameters=None
        ):

        self.mortality_rates = mortality_rates
        self.mortality_parameters = mortality_parameters

    def qx(self, policy, age: int) -> float:
        """
        Resolve mortality using policy context
        and attained age.
        """

        key = (
            policy.gender,
            age
        )

        if key not in self.mortality_rates:

            raise ValueError(
                f"No mortality rate found for "
                f"gender={policy.gender}, age={age}"
            )

        base_qx = self.mortality_rates[key]

        if self.mortality_parameters is None:

            return base_qx

        smoker_multiplier = (
            self.mortality_parameters.smoker_multiplier(
                policy.smoker_status
            )
        )

        final_qx = base_qx * smoker_multiplier

        return min(final_qx, 1.0)

    def px(self, policy, age: int) -> float:

        return 1 - self.qx(policy, age)

    def __repr__(self):

        return (
            f"MortalityTable("
            f"ages={len(self.mortality_rates)}"
            f")"
        )
    
class MortalityParameters:
    """
    Mortality adjustment parameters.

    Responsible for:
    - storing mortality multipliers
    - resolving smoker adjustments

    Does NOT:
    - perform mortality lookup
    - perform projection logic
    """

    def __init__(self, smoker_multipliers):

        self.smoker_multipliers = smoker_multipliers

    def smoker_multiplier(self, smoker_status: str) -> float:

        if smoker_status not in self.smoker_multipliers:

            raise ValueError(
                f"No smoker multiplier found for "
                f"{smoker_status}"
            )

        return self.smoker_multipliers[smoker_status]