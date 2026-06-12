import streamlit as st
import pandas as pd


def render_results_tab(
    result
):
    """
    Render capital workflow results.

    Parameters
    ----------
    result : CapitalWorkflowResult | None
    """

    if result is None:

        st.info(
            "Run the model from the Inputs tab "
            "to view results."
        )

        return

    # =====================================
    # Base Valuation
    # =====================================

    st.header(
        "Base Valuation"
    )

    st.metric(
        "BEL",
        f"{result.base_result.best_estimate_liability:,.2f}"
    )

    # =====================================
    # Univariate SCRs
    # =====================================

    st.header(
        "Univariate SCRs"
    )

    rows = []

    for scr in result.scr_results:

        rows.append(
            {
                "Category":
                    scr.aggregation_category,

                "Risk":
                    scr.risk_type,

                "Scenario":
                    scr.scenario_id,

                "SCR":
                    round(
                        scr.scr,
                        2
                    )
            }
        )

    scr_df = pd.DataFrame(
        rows
    )

    st.dataframe(
        scr_df,
        use_container_width=True,
        hide_index=True
    )

    # =====================================
    # Life SCR
    # =====================================

    if result.life_scr is not None:

        st.header(
            "Life SCR"
        )

        col1, col2 = st.columns(
            2
        )

        with col1:

            st.metric(
                "Gross",
                f"{result.life_scr.gross_scr:,.2f}"
            )

        with col2:

            st.metric(
                "Diversified",
                f"{result.life_scr.diversified_scr:,.2f}"
            )

    # =====================================
    # Market SCR
    # =====================================

    if result.market_scr is not None:

        st.header(
            "Market SCR"
        )

        col1, col2 = st.columns(
            2
        )

        with col1:

            st.metric(
                "Gross",
                f"{result.market_scr.gross_scr:,.2f}"
            )

        with col2:

            st.metric(
                "Diversified",
                f"{result.market_scr.diversified_scr:,.2f}"
            )

    # =====================================
    # BSCR
    # =====================================

    if result.bscr is not None:

        st.header(
            "BSCR"
        )

        col1, col2 = st.columns(
            2
        )

        with col1:

            st.metric(
                "Gross",
                f"{result.bscr.gross_scr:,.2f}"
            )

        with col2:

            st.metric(
                "Diversified",
                f"{result.bscr.diversified_scr:,.2f}"
            )