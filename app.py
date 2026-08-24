import streamlit as st

st.title("Real Estate Deal Analyzer")

st.write("A free tool to analyze real estate investment opportunities.")

st.header("Property Information")

purchase_price = st.number_input(
    "Purchase Price ($)",
    min_value=0,
    value=500000
)

monthly_rent = st.number_input(
    "Monthly Rent ($)",
    min_value=0,
    value=3000
)

down_payment = st.number_input(
    "Down Payment ($)",
    min_value=0,
    value=100000
)

interest_rate = st.number_input(
    "Mortgage Interest Rate (%)",
    min_value=0.0,
    value=4.5,
    step=0.1
)

amortization_years = st.number_input(
    "Amortization (Years)",
    min_value=1,
    value=25
)
annual_rent = monthly_rent * 12

st.header("Basic Analysis")

st.write(f"Annual Gross Rent: ${annual_rent:,.0f}")
