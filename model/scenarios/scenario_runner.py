from model.assumptions import (
    AssumptionSet
)

from model.scenarios.stress_registry import (
    STRESS_REGISTRY
)

from model.valuation import value_policy
from model.portfolio import Portfolio

def build_scenario_assumptions(
    base_assumptions,
    scenario
):
    """
    Construct scenario-adjusted assumptions.

    Responsibilities:
    - wrap base assumption providers
    - apply scenario overlays
    - preserve stable engine interfaces

    Does NOT:
    - perform projection logic
    - perform valuation logic
    - perform SCR calculations
    """

    providers = dict(
        base_assumptions.providers
    )
    
    for stress_name, stress_value in scenario.stresses.items():

        definition = (
            STRESS_REGISTRY[stress_name]
        )

        target_assumption = (
            definition.target_assumption
        )

        providers[target_assumption] = (
            definition.wrapper_factory(
                providers[target_assumption],
                stress_value
            )
        )

    return AssumptionSet(
        providers
    )

def run_scenario(
    model_object,
    base_assumptions,
    scenario,
    return_breakdown=False
):
    """
    Run valuation under a scenario.

    Responsibilities:
    - construct scenario-adjusted assumptions
    - orchestrate stressed valuation runs
    - preserve scenario-agnostic engine behaviour

    Supports:
    - Policy
    - Portfolio
    """

    scenario_assumptions = (
        build_scenario_assumptions(
            base_assumptions,
            scenario
        )
    )

    if isinstance(model_object, Portfolio):

        return model_object.value(
            scenario_assumptions,
            return_breakdown=return_breakdown
        )

    return value_policy(
        model_object,
        scenario_assumptions,
        return_breakdown=return_breakdown
    )