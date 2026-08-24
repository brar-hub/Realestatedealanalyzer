import streamlit as st

st.title("Real Estate Deal Analyzer")

st.write(
    "A free tool to analyze real estate investment opportunities."
)

# -----------------------------
# Property Information
# -----------------------------

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

# -----------------------------
# Operating Expenses
# -----------------------------

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

# -----------------------------
# Calculations
# -----------------------------

annual_rent = monthly_rent * 12

loan_amount = purchase_price - down_payment

monthly_rate = interest_rate / 100 / 12

number_of_payments = amortization_years * 12

if monthly_rate > 0 and loan_amount > 0:
    monthly_mortgage_payment = loan_amount * (
        monthly_rate * (1 + monthly_rate) ** number_of_payments
    ) / (
        (1 + monthly_rate) ** number_of_payments - 1
    )
elif loan_amount > 0:
    monthly_mortgage_payment = loan_amount / number_of_payments
else:
    monthly_mortgage_payment = 0

annual_mortgage_payments = monthly_mortgage_payment * 12

vacancy_loss = annual_rent * (vacancy_rate / 100)

effective_gross_income = annual_rent - vacancy_loss

total_operating_expenses = (
    annual_property_tax
    + annual_insurance
    + annual_maintenance
)

net_operating_income = (
    effective_gross_income
    - total_operating_expenses
)

annual_cash_flow = (
    net_operating_income
    - annual_mortgage_payments
)

monthly_cash_flow = annual_cash_flow / 12

# -----------------------------
# Basic Analysis
# -----------------------------

st.header("Basic Analysis")

st.write(f"Annual Gross Rent: ${annual_rent:,.0f}")

st.write(f"Vacancy Loss: ${vacancy_loss:,.0f}")

st.write(
    f"Effective Gross Income: ${effective_gross_income:,.0f}"
)

st.write(
    f"Operating Expenses: ${total_operating_expenses:,.0f}"
)

st.write(
    f"Net Operating Income: ${net_operating_income:,.0f}"
)

st.write(f"Loan Amount: ${loan_amount:,.0f}")

st.write(
    f"Monthly Mortgage Payment: ${monthly_mortgage_payment:,.0f}"
)

st.write(
    f"Annual Mortgage Payments: ${annual_mortgage_payments:,.0f}"
)

st.write(f"Annual Cash Flow: ${annual_cash_flow:,.0f}")

st.write(f"Monthly Cash Flow: ${monthly_cash_flow:,.0f}")
