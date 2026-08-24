import streamlit as st

# ============================================================
# WTM. — Wealth That Matters
# Real Estate Deal Analyzer
# ============================================================

st.set_page_config(
    page_title="WTM. Real Estate Deal Analyzer",
    page_icon="🏠",
    layout="centered"
)

# -----------------------------
# WTM Branding
# -----------------------------

st.markdown(
    """
    <div style="text-align:center; padding:10px 0 20px 0;">
        <div style="font-size:42px; font-weight:800;">
            WTM.
        </div>
        <div style="font-size:16px;">
            Wealth That Matters
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.title("Real Estate Deal Analyzer")

st.write(
    "A free tool to analyze real estate investment opportunities."
)

# ============================================================
# Property Information
# ============================================================

st.header("Property Information")

purchase_price = st.number_input(
    "Purchase Price ($)",
    min_value=0,
    value=500000,
    help=(
        "The agreed purchase price of the property. "
        "This is the amount used to calculate the property's "
        "operating return and financing requirements."
    )
)

monthly_rent = st.number_input(
    "Monthly Rent ($)",
    min_value=0,
    value=3000,
    help=(
        "The total rent you expect to collect each month. "
        "If the property has multiple units, enter the combined "
        "monthly rental income."
    )
)

down_payment = st.number_input(
    "Down Payment ($)",
    min_value=0,
    value=100000,
    help=(
        "The amount of your own money used toward purchasing "
        "the property. A larger down payment generally reduces "
        "the mortgage payment but requires more upfront capital."
    )
)

interest_rate = st.number_input(
    "Mortgage Interest Rate (%)",
    min_value=0.0,
    value=4.5,
    step=0.1,
    help=(
        "The annual interest rate charged on the mortgage. "
        "This is used to estimate the required mortgage payment."
    )
)

amortization_years = st.number_input(
    "Amortization (Years)",
    min_value=1,
    value=25,
    help=(
        "The total period over which the mortgage is scheduled "
        "to be repaid. A longer amortization generally lowers "
        "the monthly payment but increases total interest paid."
    )
)

# ============================================================
# Operating Expenses
# ============================================================

st.header("Operating Expenses")

annual_property_tax = st.number_input(
    "Annual Property Tax ($)",
    min_value=0,
    value=4000,
    help=(
        "The estimated property taxes paid to the local government "
        "each year."
    )
)

annual_insurance = st.number_input(
    "Annual Insurance ($)",
    min_value=0,
    value=1500,
    help=(
        "The estimated annual cost of property insurance."
    )
)

annual_maintenance = st.number_input(
    "Annual Maintenance ($)",
    min_value=0,
    value=3000,
    help=(
        "An estimate of the property's annual maintenance and repair "
        "costs. This can include repairs, replacements, and routine "
        "maintenance."
    )
)

vacancy_rate = st.number_input(
    "Vacancy Rate (%)",
    min_value=0.0,
    max_value=100.0,
    value=5.0,
    step=0.5,
    help=(
        "The estimated percentage of rental income lost because "
        "the property is vacant or the rent is not collected. "
        "For example, a 5% vacancy rate assumes approximately "
        "95% of potential rent is collected. "
        "It can be estimated as expected vacant time divided by "
        "total available rental time."
    )
)

# ============================================================
# Calculations
# ============================================================

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

# ============================================================
# Investment Metrics
# ============================================================

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

# Break-even Rent
annual_non_mortgage_costs = (
    total_operating_expenses
    + annual_mortgage_payments
)

if vacancy_rate < 100:
    break_even_monthly_rent = (
        annual_non_mortgage_costs / 12
    ) / (1 - vacancy_rate / 100)
else:
    break_even_monthly_rent = 0

# ============================================================
# Deal Health
# ============================================================

if monthly_cash_flow > 200:
    deal_health = "🟢 Strong"
elif monthly_cash_flow >= 0:
    deal_health = "🟡 Marginal"
else:
    deal_health = "🔴 Needs Attention"

# ============================================================
# Quick Deal Analysis
# ============================================================

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
        "from its current rental income. However, the final decision "
        "should also consider financing terms, property condition, "
        "future expenses, taxes, appreciation, and local market "
        "conditions."
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

# ============================================================
# Key Metrics
# ============================================================

st.header("Key Metrics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Monthly Cash Flow",
        f"${monthly_cash_flow:,.0f}",
        help=(
            "The estimated amount left each month after rental "
            "income, operating expenses, and mortgage payments."
        )
    )

with col2:
    st.metric(
        "Cap Rate",
        f"{cap_rate:.2f}%",
        help=(
            "Cap Rate measures the property's annual operating income "
            "relative to its purchase price, before mortgage financing. "
            "It is calculated as NOI divided by purchase price."
        )
    )

with col3:
    st.metric(
        "Cash-on-Cash Return",
        f"{cash_on_cash_return:.2f}%",
        help=(
            "Cash-on-Cash Return measures annual cash flow relative "
            "to the cash you invested in the property. "
            "It is calculated as annual cash flow divided by "
            "initial cash investment."
        )
    )

# ============================================================
# Detailed Analysis
# ============================================================

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

# ============================================================
# Disclaimer
# ============================================================

st.divider()

st.caption(
    "WTM. — Wealth That Matters"
)

st.caption(
    "This analysis is an estimate based on the information entered "
    "and is provided for educational and informational purposes only. "
    "It is not financial, investment, tax, legal, or real estate advice. "
    "Users should independently verify all assumptions and consult "
    "qualified professionals before making financial decisions."
)
