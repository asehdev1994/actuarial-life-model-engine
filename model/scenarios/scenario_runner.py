from model.assumptions import (
    AssumptionSet
)

from model.scenarios.stressed_assumptions import (
    StressedMortalityTable,
    StressedLapseTable,
    StressedYieldCurve,
    StressedExpenseTable
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

    stressed_mortality = (
        StressedMortalityTable(
            base_assumptions.mortality,
            mortality_multiplier=
                scenario.mortality_multiplier
        )
    )

    stressed_lapse = (
        StressedLapseTable(
            base_assumptions.lapse,
            lapse_multiplier=
                scenario.lapse_multiplier
        )
    )

    stressed_interest = (
        StressedYieldCurve(
            base_assumptions.interest,
            interest_rate_shift=
                scenario.interest_rate_shift
        )
    )

    stressed_expenses = (
        StressedExpenseTable(
            base_assumptions.expenses_provider,
            expense_multiplier=
                scenario.expense_multiplier
        )
    )

    return AssumptionSet(
        mortality=stressed_mortality,
        interest=stressed_interest,
        lapse=stressed_lapse,
        expenses=stressed_expenses
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