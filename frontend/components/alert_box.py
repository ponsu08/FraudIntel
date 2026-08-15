import streamlit as st


def success(message):

    st.success(
        "✅ " + message
    )


def warning(message):

    st.warning(
        "⚠ " + message
    )


def danger(message):

    st.error(
        "🚨 " + message
    )


def info(message):

    st.info(
        "ℹ " + message
    )