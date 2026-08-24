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

loan_amount = max(purchase_price - down_payment, 0)

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

# Cap Rate
if purchase_price > 0:
    cap_rate = (
        net_operating_income / purchase_price
    ) * 100
else:
    cap_rate = 0

# Cash-on-Cash Return
if down_payment > 0:
    cash_on_cash_return = (
        annual_cash_flow / down_payment
    ) * 100
else:
    cash_on_cash_return = 0

# Break-even monthly rent
annual_non_mortgage_costs = (
    total_operating_expenses
    + annual_mortgage_payments
)

break_even_monthly_rent = (
    annual_non_mortgage_costs / 12
) / (1 - vacancy_rate / 100)

# -----------------------------
# Deal Health
# -----------------------------

if monthly_cash_flow > 200:
    deal_health = "🟢 Strong"
elif monthly_cash_flow >= 0:
    deal_health = "🟡 Marginal"
else:
    deal_health = "🔴 Needs Attention"

# -----------------------------
# Deal Summary
# -----------------------------

st.header("Quick Deal Analysis")

st.subheader(f"Deal Health: {deal_health}")

if monthly_cash_flow > 0:

    st.write(
        f"This property is estimated to generate approximately "
        f"${monthly_cash_flow:,.0f} per month in positive cash flow "
        f"after the estimated operating expenses and mortgage payment."
    )

    st.write(
        f"At the current assumptions, the property generates a "
        f"{cap_rate:.2f}% cap rate and a "
        f"{cash_on_cash_return:.2f}% cash-on-cash return."
    )

    st.write(
        f"The estimated break-even rent is approximately "
        f"${break_even_monthly_rent:,.0f} per month."
    )

    st.write(
        "Overall, the deal appears capable of supporting itself "
        "from its current rental income, although the final decision "
        "should also consider financing terms, property condition, "
        "future expenses, taxes, appreciation, and local market conditions."
    )

elif monthly_cash_flow >= 0:

    st.write(
        "This property is approximately cash-flow neutral under "
        "the assumptions provided."
    )

    st.write(
        f"The property produces a {cap_rate:.2f}% cap rate, but the "
        f"margin of safety is relatively small."
    )

    st.write(
        f"The estimated break-even rent is approximately "
        f"${break_even_monthly_rent:,.0f} per month."
    )

    st.write(
        "A small increase in expenses, vacancy, or financing costs "
        "could push the property into negative cash flow."
    )

else:

    st.write(
        f"This property is estimated to lose approximately "
        f"${abs(monthly_cash_flow):,.0f} per month under the "
        f"current assumptions."
    )

    st.write(
        f"The property has a {cap_rate:.2f}% cap rate, but the "
        f"current financing structure results in negative cash flow."
    )

    st.write(
        f"The estimated break-even rent is approximately "
        f"${break_even_monthly_rent:,.0f} per month."
    )

    st.write(
        "You may want to investigate a lower purchase price, "
        "different financing, a larger down payment, higher achievable "
        "rent, or lower operating expenses."
    )

st.caption(
    "This analysis is an estimate based on the information entered "
    "and is not financial, tax, legal, or investment advice."
)

# -----------------------------
# Detailed Analysis
# -----------------------------

st.header("Detailed Analysis")

st.write(
    f"Annual Gross Rent: ${annual_rent:,.0f}"
)

st.write(
    f"Vacancy Loss: ${vacancy_loss:,.0f}"
)

st.write(
    f"Effective Gross Income: ${effective_gross_income:,.0f}"
)

st.write(
    f"Operating Expenses: ${total_operating_expenses:,.0f}"
)

st.write(
    f"Net Operating Income: ${net_operating_income:,.0f}"
)

st.write(
    f"Cap Rate: {cap_rate:.2f}%"
)

st.write(
    f"Loan Amount: ${loan_amount:,.0f}"
)

st.write(
    f"Monthly Mortgage Payment: ${monthly_mortgage_payment:,.0f}"
)

st.write(
    f"Annual Mortgage Payments: ${annual_mortgage_payments:,.0f}"
)

st.write(
    f"Annual Cash Flow: ${annual_cash_flow:,.0f}"
)

st.write(
    f"Monthly Cash Flow: ${monthly_cash_flow:,.0f}"
)

st.write(
    f"Cash-on-Cash Return: {cash_on_cash_return:.2f}%"
)

st.write(
    f"Break-even Monthly Rent: ${break_even_monthly_rent:,.0f}"
)
