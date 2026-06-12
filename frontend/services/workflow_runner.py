from model.capital.capital_workflow import (
    run_capital_workflow
)


def execute_workflow(
    workflow_config
):
    """
    Execute the actuarial model
    using a CapitalWorkflowConfig.
    """

    return run_capital_workflow(
        workflow_config
    )