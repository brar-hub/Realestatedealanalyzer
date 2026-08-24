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

annual_rent = monthly_rent * 12

st.header("Basic Analysis")

st.write(f"Annual Gross Rent: ${annual_rent:,.0f}")
