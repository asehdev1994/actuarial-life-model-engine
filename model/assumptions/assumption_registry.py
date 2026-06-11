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
        config_attributes=[
            "mortality_table_path",
            "mortality_parameter_path"
        ],
        loader=load_mortality_provider,
        null_provider_factory=NullMortalityProvider
    ),

    "interest": AssumptionDefinition(
        name="interest",
        config_attributes=[
            "yield_curve_path"
        ],
        loader=load_yield_curve,
        null_provider_factory=NullInterestProvider
    ),

    "lapse": AssumptionDefinition(
        name="lapse",
        config_attributes=[
            "lapse_table_path"
        ],
        loader=load_lapse_table,
        null_provider_factory=NullLapseProvider
    ),

    "expense": AssumptionDefinition(
        name="expense",
        config_attributes=[
            "expense_table_path"
        ],
        loader=load_expense_table,
        null_provider_factory=NullExpenseProvider
    )
}