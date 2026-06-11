"""
Central stress registry.

Defines officially supported
scenario calibration interface.
"""

from model.scenarios.stress_definition import (

    StressDefinition

)

from model.scenarios.stressed_assumptions import (

    StressedMortalityTable,

    StressedLapseTable,

    StressedYieldCurve,

    StressedExpenseTable

)

STRESS_REGISTRY = {

    "mortality_multiplier":

        StressDefinition(

            name="mortality_multiplier",

            target_assumption="mortality",

            wrapper_factory=StressedMortalityTable

        ),

    "lapse_multiplier":

        StressDefinition(

            name="lapse_multiplier",

            target_assumption="lapse",

            wrapper_factory=StressedLapseTable

        ),

    "interest_rate_shift":

        StressDefinition(

            name="interest_rate_shift",

            target_assumption="interest",

            wrapper_factory=StressedYieldCurve

        ),

    "expense_multiplier":

        StressDefinition(

            name="expense_multiplier",

            target_assumption="expense",

            wrapper_factory=StressedExpenseTable

        )

}