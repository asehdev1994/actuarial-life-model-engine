from model.config import (
    AssumptionConfig,
    ScenarioConfig,
    CorrelationConfig,
    CapitalWorkflowConfig
)


def build_workflow_config(
    portfolio_path,
    assumption_paths,
    scenario_path,
    correlation_paths,
    return_breakdown=False
):
    """
    Construct a CapitalWorkflowConfig
    from persisted frontend inputs.
    """

    assumption_config = (
        AssumptionConfig(
            values=assumption_paths
        )
    )

    scenario_config = (
        ScenarioConfig(
            scenario_path=scenario_path
        )
    )

    correlation_config = (
        CorrelationConfig(
            life_correlation_path=(
                correlation_paths["life"]
            ),

            market_correlation_path=(
                correlation_paths["market"]
            ),

            bscr_correlation_path=(
                correlation_paths["bscr"]
            )
        )
    )

    return CapitalWorkflowConfig(
        portfolio_path=(
            portfolio_path
        ),

        assumption_config=(
            assumption_config
        ),

        scenario_config=(
            scenario_config
        ),

        correlation_config=(
            correlation_config
        ),

        return_breakdown=(
            return_breakdown
        )
    )