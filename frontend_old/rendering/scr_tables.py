import pandas as pd
import streamlit as st


def render_scr_table(
    workflow_result
):

    rows = []

    for scr in workflow_result.scr_results:

        rows.append({
            "Scenario":
                scr.scenario_id,

            "Risk":
                scr.risk_type,

            "Category":
                scr.aggregation_category,

            "Base BEL":
                round(
                    scr.base_bel,
                    2
                ),

            "Stressed BEL":
                round(
                    scr.stressed_bel,
                    2
                ),

            "SCR":
                round(
                    scr.scr,
                    2
                )
        })

    df = pd.DataFrame(rows)

    st.subheader(
        "SCR Results"
    )

    st.dataframe(df)

    if workflow_result.life_scr:

        st.metric(
            "Life SCR",
            round(
                workflow_result.life_scr.diversified_scr,
                2
            )
        )

    if workflow_result.market_scr:

        st.metric(
            "Market SCR",
            round(
                workflow_result.market_scr.diversified_scr,
                2
            )
        )

    if workflow_result.bscr:

        st.metric(
            "BSCR",
            round(
                workflow_result.bscr.diversified_scr,
                2
            )
        )