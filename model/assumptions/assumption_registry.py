from model.assumptions.assumption_definition import (
    AssumptionDefinition
)

from model.assumptions.assumption_loader import (
    load_mortality_table,
    load_mortality_provider,
    load_yield_curve,
    load_lapse_table,
    load_expense_table
)

from model.assumptions.null_providers import(
    NullLapseProvider,
    NullExpenseProvider,
    NullInterestProvider,
    NullMortalityProvider
)

ASSUMPTION_REGISTRY = {

    "mortality": AssumptionDefinition(
        name="mortality",
        display_name= "Mortality",
        config_attributes=[
            "mortality_table_path",
            "mortality_parameter_path"
        ],
        loader=load_mortality_provider,
        description=(
            "Base mortality table and "
            "mortality parameter file."
        ),
        null_provider_factory=NullMortalityProvider
    ),

    "interest": AssumptionDefinition(
        name="interest",
        display_name="Interest",
        config_attributes=[
            "yield_curve_path"
        ],
        loader=load_yield_curve,
        description=(
            "Yield curve used for "
            "discounting cashflows."
        ),
        null_provider_factory=NullInterestProvider
    ),

    "lapse": AssumptionDefinition(
        name="lapse",
        display_name="Lapse",
        config_attributes=[
            "lapse_table_path"
        ],
        loader=load_lapse_table,
        description=(
            "Policy Lapse assumption table."
        ),
        null_provider_factory=NullLapseProvider
    ),

    "expense": AssumptionDefinition(
        name="expense",
        display_name="Expense",
        config_attributes=[
            "expense_table_path"
        ],
        loader=load_expense_table,
        description=(
            "Acquisition and maintenence "
            "expense assumptions."
        ),
        null_provider_factory=NullExpenseProvider
    )
}