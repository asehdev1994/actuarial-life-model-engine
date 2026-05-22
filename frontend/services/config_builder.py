from model.config import (
    AssumptionConfig,
    ScenarioConfig,
    CorrelationConfig,
    CapitalWorkflowConfig
)


def build_workflow_config(
    uploaded_paths
):

    assumption_config = (
        AssumptionConfig(
            mortality_table_path=uploaded_paths[
                "mortality_table"
            ],

            mortality_parameter_path=uploaded_paths.get(
                "mortality_parameters"
            ),

            yield_curve_path=uploaded_paths[
                "yield_curve"
            ],

            lapse_table_path=uploaded_paths.get(
                "lapse_table"
            ),

            expense_table_path=uploaded_paths.get(
                "expense_table"
            )
        )
    )

    scenario_config = (
        ScenarioConfig(
            scenario_path=uploaded_paths[
                "scenario_csv"
            ]
        )
    )

    correlation_config = (
        CorrelationConfig(
            life_correlation_path=uploaded_paths[
                "life_correlation"
            ],

            market_correlation_path=uploaded_paths[
                "market_correlation"
            ],

            bscr_correlation_path=uploaded_paths[
                "bscr_correlation"
            ]
        )
    )

    return CapitalWorkflowConfig(
        portfolio_path=uploaded_paths[
            "portfolio"
        ],

        assumption_config=assumption_config,

        scenario_config=scenario_config,

        correlation_config=correlation_config,

        return_breakdown=False
    )