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

loan_amount = purchase_price - down_payment

monthly_rate = interest_rate / 100 / 12

number_of_payments = amortization_years * 12

if monthly_rate > 0:
    monthly_mortgage_payment = loan_amount * (
        monthly_rate * (1 + monthly_rate) ** number_of_payments
    ) / (
        (1 + monthly_rate) ** number_of_payments - 1
    )
else:
    monthly_mortgage_payment = loan_amount / number_of_payments

st.header("Basic Analysis")

st.header("Operating Expenses")

annual_property_tax = st.number_input(
    "Annual Property Tax ($)",
    min_value=0,
    value=4000
)

annual_insurance = st.number_input(
    "Annual Insurance ($)",
    min_value=0,
    value=1500
)

annual_maintenance = st.number_input(
    "Annual Maintenance ($)",
    min_value=0,
    value=3000
)

vacancy_rate = st.number_input(
    "Vacancy Rate (%)",
    min_value=0.0,
    max_value=100.0,
    value=5.0,
    step=0.5
)
st.write(f"Annual Gross Rent: ${annual_rent:,.0f}")

st.write(f"Loan Amount: ${loan_amount:,.0f}")
st.write(f"Monthly Mortgage Payment: ${monthly_mortgage_payment:,.0f}")
st.write(f"Annual Mortgage Payments: ${monthly_mortgage_payment * 12:,.0f}")
