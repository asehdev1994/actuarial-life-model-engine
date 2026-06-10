from model.assumptions.assumption_definition import (
    AssumptionDefinition
)

from model.assumptions.assumption_loader import (
    load_mortality_table,
    load_yield_curve,
    load_lapse_table,
    load_expense_table
)

ASSUMPTION_REGISTRY = {

    "mortality": AssumptionDefinition(
        name="mortality",
        config_attribute="mortality_table_path",
        loader=load_mortality_table
    ),

    "interest": AssumptionDefinition(
        name="interest",
        config_attribute="yield_curve_path",
        loader=load_yield_curve
    ),

    "lapse": AssumptionDefinition(
        name="lapse",
        config_attribute="lapse_table_path",
        loader=load_lapse_table
    ),

    "expense": AssumptionDefinition(
        name="expense",
        config_attribute="expense_table_path",
        loader=load_expense_table
    )
}