"""
Capital workflow orchestration layer.

Responsibilities:
- orchestrate scenario execution
- generate SCR results
- coordinate aggregation sequencing
- package workflow outputs

Does NOT:
- run projection mechanics
- run valuation mechanics
- apply stress logic
- perform aggregation mathematics
"""

from collections import defaultdict

from model.capital.scr_calculator import (
    calculate_scr
)

from model.capital.aggregation import (
    aggregate_life_scr,
    aggregate_market_scr,
    aggregate_basic_scr
)

from model.scenarios.scenario_loader import (
    load_scenarios
)

from model.scenarios.scenario_runner import (
    run_scenario
)

from model.results.workflow_results import (
    CapitalWorkflowResult
)

from model.assumptions import (
    AssumptionSet
)

from model.assumptions.assumption_loader import (
    load_mortality_table,
    load_mortality_parameters,
    load_yield_curve,
    load_lapse_table,
    load_expense_table
)

from model.data.portfolio_loader import (
    load_portfolio_csv
)

from model.capital.correlation_loader import (
    load_correlation_matrix
)

from model.config import (
    AssumptionConfig,
    CorrelationConfig,
    ScenarioConfig,
    CapitalWorkflowConfig
)

from model.portfolio import Portfolio
from model.valuation import value_policy

from model.assumptions.assumption_registry import (
    ASSUMPTION_REGISTRY
)


def run_capital_framework(
    model_object,
    assumptions,
    scenario_path,
    life_correlation_matrix,
    market_correlation_matrix,
    bscr_correlation_matrix,
    return_breakdown=False
):
    """
    Run full capital workflow.

    Workflow:
    - base valuation
    - stressed scenario valuation
    - SCR generation
    - aggregation sequencing
    - BSCR calculation
    """

    # =========================
    # Base valuation
    # =========================

    if isinstance(model_object, Portfolio):

        base_result = model_object.value(
            assumptions,
            return_breakdown=return_breakdown
        )

    else:

        base_result = value_policy(
            model_object,
            assumptions,
            return_breakdown=return_breakdown
        )

    # =========================
    # Load scenarios
    # =========================

    scenarios = load_scenarios(
        scenario_path
    )

    enabled_scenarios = [
        scenario
        for scenario in scenarios
        if scenario.enabled
    ]

    # =========================
    # Run stressed scenarios
    # =========================

    scenario_results = {}

    scr_results = []

    for scenario in enabled_scenarios:

        stressed_result = run_scenario(
            model_object=model_object,
            base_assumptions=assumptions,
            scenario=scenario,
            return_breakdown=return_breakdown
        )

        scenario_results[
            scenario.scenario_id
        ] = stressed_result

        scr_result = calculate_scr(
            base_result=base_result,
            stressed_result=stressed_result,
            scenario=scenario
        )

        scr_results.append(
            scr_result
        )

    # =========================
    # Group SCRs
    # =========================

    grouped_scrs = defaultdict(list)

    for scr in scr_results:

        grouped_scrs[
            scr.aggregation_category
        ].append(scr)

    # =========================
    # Aggregate life SCR
    # =========================

    life_scr = None

    if grouped_scrs["life"]:

        life_scr = aggregate_life_scr(
            scr_results=grouped_scrs["life"],
            correlation_matrix=(
                life_correlation_matrix
            )
        )

    # =========================
    # Aggregate market SCR
    # =========================

    market_scr = None

    if grouped_scrs["market"]:

        market_scr = aggregate_market_scr(
            scr_results=grouped_scrs["market"],
            correlation_matrix=(
                market_correlation_matrix
            )
        )

    # =========================
    # Aggregate BSCR
    # =========================

    bscr = None

    if (
        life_scr is not None
        and market_scr is not None
    ):

        bscr = aggregate_basic_scr(
            life_scr=life_scr,
            market_scr=market_scr,
            correlation_matrix=(
                bscr_correlation_matrix
            )
        )

    # =========================
    # Package results
    # =========================

    return CapitalWorkflowResult(
        base_result=base_result,
        scenario_results=scenario_results,
        scr_results=scr_results,
        life_scr=life_scr,
        market_scr=market_scr,
        bscr=bscr
    )

def load_workflow_assumptions(
    config:AssumptionConfig
):
    """
    Load assumptions for workflow execution.

    Responsibilities:
    - orchestrate provider loading
    - construct unified AssumptionSet

    Does NOT:
    - perform validation logic
    - perform actuarial calculations
    """

    loaded_assumptions = {}

    mortality_parameters = None

    if (
        config.mortality_parameter_path
        is not None
    ):

        mortality_parameters = (
            load_mortality_parameters(
                config.mortality_parameter_path
            )
        )

    for definition in ASSUMPTION_REGISTRY.values():

        path = getattr(
            config,
            definition.config_attribute
        )

        if path is None:
            
            if (
                definition.null_provider_factory
                is not None
            ):
                loaded_assumptions[
                    definition.name
                ] = (
                    definition.null_provider_factory()
                )
            continue

        provider = definition.loader(
            path
        )

        loaded_assumptions[
            definition.name
        ] = provider

    if (
        mortality_parameters is not None
    ):
        loaded_assumptions[
            "mortality"
        ].mortality_parameters = (
            mortality_parameters
        )

    return AssumptionSet(
        providers = loaded_assumptions
    )

def load_workflow_correlations(
    config: CorrelationConfig
):
    """
    Load workflow correlation matrices.
    """

    return {
        "life": load_correlation_matrix(
            config.life_correlation_path
        ),

        "market": load_correlation_matrix(
            config.market_correlation_path
        ),

        "bscr": load_correlation_matrix(
            config.bscr_correlation_path
        )
    }

def run_capital_workflow(
    config: CapitalWorkflowConfig
):
    """
    High-level capital workflow entry point.

    Responsibilities:
    - orchestrate workflow-owned loading
    - execute capital framework
    - centralise workflow configuration

    Intended future usage:
    - Streamlit backend
    - local execution workflows
    - configuration-driven execution
    """

    assumptions = (
        load_workflow_assumptions(
            config.assumption_config
        )
    )

    portfolio = (
        load_workflow_portfolio(
            config.portfolio_path
        )
    )

    correlations = (
        load_workflow_correlations(
            config.correlation_config
        )
    )

    return run_capital_framework(
        model_object=portfolio,

        assumptions=assumptions,

        scenario_path=(
            config.scenario_config.scenario_path
        ),

        life_correlation_matrix=(
            correlations["life"]
        ),

        market_correlation_matrix=(
            correlations["market"]
        ),

        bscr_correlation_matrix=(
            correlations["bscr"]
        ),

        return_breakdown=(
            config.return_breakdown
        )
    )

def load_workflow_portfolio(
    portfolio_path
):
    """
    Load workflow portfolio.
    """

    return load_portfolio_csv(
        portfolio_path
    )