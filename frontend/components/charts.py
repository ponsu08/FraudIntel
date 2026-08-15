import pandas as pd
import plotly.express as px
import streamlit as st


def risk_pie_chart(safe, fraud):

    df = pd.DataFrame(
        {
            "Category": ["Safe", "Fraud"],
            "Count": [safe, fraud]
        }
    )

    fig = px.pie(
        df,
        names="Category",
        values="Count",
        hole=0.45,
        title="Fraud Detection Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


def scan_bar_chart(data):

    df = pd.DataFrame(data)

    fig = px.bar(
        df,
        x="Module",
        y="Scans",
        title="Module Wise Scans"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


def risk_line_chart(df):

    fig = px.line(
        df,
        x="Date",
        y="Risk",
        title="Daily Risk Score"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )