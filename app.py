import streamlit as st
import pandas as pd

# ============================================================
# WTM. — Wealth That Matters
# Real Estate Deal Analyzer
# ============================================================

st.set_page_config(
    page_title="WTM. Real Estate Deal Analyzer",
    page_icon="🏠",
    layout="centered"
)

# ============================================================
# WTM BRANDING
# ============================================================

st.markdown(
    """
    <div style="text-align:center; padding:10px 0 20px 0;">
        <div style="font-size:44px; font-weight:800;">
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
    "A free tool to analyze real estate investment opportunities "
    "and understand how a property could build wealth over time."
)

# ============================================================
# PROPERTY INFORMATION
# ============================================================

st.header("Property Information")

purchase_price = st.number_input(
    "Purchase Price ($)",
    min_value=0.0,
    value=500000.0,
    step=5000.0,
    help=(
        "The agreed purchase price of the property. "
        "This is used to calculate the property's operating return "
        "and financing requirements."
    )
)

monthly_rent = st.number_input(
    "Monthly Rent ($)",
    min_value=0.0,
    value=3000.0,
    step=100.0,
    help=(
        "The total rent expected each month. "
        "For a multi-unit property, enter the combined rental income."
    )
)

down_payment = st.number_input(
    "Down Payment ($)",
    min_value=0.0,
    value=100000.0,
    step=5000.0,
    help=(
        "The amount of your own money invested toward the purchase. "
        "A larger down payment reduces the mortgage but requires "
        "more cash upfront."
    )
)

interest_rate = st.number_input(
    "Mortgage Interest Rate (%)",
    min_value=0.0,
    value=5.14,
    step=0.05,
    help=(
        "The annual mortgage interest rate used to estimate "
        "the monthly mortgage payment."
    )
)

amortization_years = st.number_input(
    "Amortization (Years)",
    min_value=1,
    max_value=50,
    value=25,
    step=1,
    help=(
        "The period over which the mortgage is scheduled to be repaid. "
        "A longer amortization generally lowers monthly payments "
        "but increases total interest paid."
    )
)

# ============================================================
# OPERATING EXPENSES
# ============================================================

st.header("Operating Expenses")

annual_property_tax = st.number_input(
    "Annual Property Tax ($)",
    min_value=0.0,
    value=4000.0,
    step=250.0,
    help=(
        "Estimated property taxes paid to the local government each year."
    )
)

annual_insurance = st.number_input(
    "Annual Insurance ($)",
    min_value=0.0,
    value=1500.0,
    step=100.0,
    help=(
        "Estimated annual cost of insuring the property."
    )
)

annual_maintenance = st.number_input(
    "Annual Maintenance ($)",
    min_value=0.0,
    value=3000.0,
    step=250.0,
    help=(
        "Estimated annual maintenance and repair costs. "
        "This may include routine repairs, replacements and upkeep."
    )
)

vacancy_rate = st.number_input(
    "Vacancy Rate (%)",
    min_value=0.0,
    max_value=100.0,
    value=5.0,
    step=0.5,
    help=(
        "The estimated percentage of potential rental income lost "
        "because the property is vacant or rent is not collected. "
        "For example, 5% assumes approximately 95% of potential "
        "rent is collected."
    )
)

# ============================================================
# LONG-TERM ASSUMPTIONS
# ============================================================

st.header("Long-Term Growth Assumptions")

st.write(
    "These assumptions are used only to illustrate how the investment "
    "could evolve over time. They are not predictions."
)

projection_years = st.slider(
    "Projection Period (Years)",
    min_value=1,
    max_value=30,
    value=10,
    help=(
        "How many years you want the wealth projection to cover."
    )
)

appreciation_rate = st.number_input(
    "Annual Property Appreciation (%)",
    min_value=-20.0,
    max_value=20.0,
    value=3.0,
    step=0.5,
    help=(
        "The assumed annual change in the property's market value. "
        "This is appreciation, not tax depreciation or CCA."
    )
)

rent_growth_rate = st.number_input(
    "Annual Rent Growth (%)",
    min_value=-20.0,
    max_value=20.0,
    value=2.0,
    step=0.5,
    help=(
        "The assumed annual growth in rental income."
    )
)

expense_growth_rate = st.number_input(
    "Annual Expense Growth (%)",
    min_value=-20.0,
    max_value=20.0,
    value=2.0,
    step=0.5,
    help=(
        "The assumed annual growth in operating expenses."
    )
)

# ============================================================
# CORE CALCULATIONS
# ============================================================

annual_rent = monthly_rent * 12

loan_amount = max(purchase_price - down_payment, 0)

monthly_rate = interest_rate / 100 / 12

number_of_payments = amortization_years * 12

if loan_amount > 0 and number_of_payments > 0:

    if monthly_rate > 0:
        monthly_mortgage_payment = loan_amount * (
            monthly_rate * (1 + monthly_rate) ** number_of_payments
        ) / (
            (1 + monthly_rate) ** number_of_payments - 1
        )
    else:
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
# INVESTMENT METRICS
# ============================================================

if purchase_price > 0:
    cap_rate = (
        net_operating_income / purchase_price
    ) * 100
else:
    cap_rate = 0

if down_payment > 0:
    cash_on_cash_return = (
        annual_cash_flow / down_payment
    ) * 100
else:
    cash_on_cash_return = 0

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
# DEAL HEALTH
# ============================================================

if monthly_cash_flow > 200:
    deal_health = "🟢 Strong"

elif monthly_cash_flow >= 0:
    deal_health = "🟡 Marginal"

else:
    deal_health = "🔴 Needs Attention"

# ============================================================
# QUICK DEAL ANALYSIS
# ============================================================

st.header("Quick Deal Analysis")

st.subheader(f"Deal Health: {deal_health}")

if monthly_cash_flow > 0:

    st.write(
        f"This property is estimated to generate approximately "
        f"${monthly_cash_flow:,.0f} per month in positive cash flow "
        f"after the estimated operating expenses and mortgage payment."
    )

elif monthly_cash_flow == 0:

    st.write(
        "This property is approximately cash-flow neutral under "
        "the assumptions provided."
    )

else:

    st.write(
        f"This property is estimated to lose approximately "
        f"${abs(monthly_cash_flow):,.0f} per month under the "
        f"current assumptions."
    )

st.write(
    f"The property generates a {cap_rate:.2f}% cap rate and a "
    f"{cash_on_cash_return:.2f}% cash-on-cash return."
)

st.write(
    f"The estimated break-even rent is approximately "
    f"${break_even_monthly_rent:,.0f} per month."
)

if monthly_rent >= break_even_monthly_rent:

    st.success(
        "Based on the current assumptions, the expected rent is "
        "at or above the estimated break-even level."
    )

else:

    st.warning(
        "Based on the current assumptions, the expected rent is "
        "below the estimated break-even level."
    )

st.info(
    "This analysis looks at the property's estimated operating "
    "performance and financing. A property can still be a good or "
    "bad investment for reasons beyond cash flow, including "
    "appreciation, financing, taxes, condition, liquidity and risk."
)

# ============================================================
# KEY METRICS
# ============================================================

st.header("Key Metrics")

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Monthly Cash Flow",
        f"${monthly_cash_flow:,.0f}",
        help=(
            "Estimated money left each month after rental income, "
            "operating expenses and mortgage payments."
        )
    )

with col2:

    st.metric(
        "Cap Rate",
        f"{cap_rate:.2f}%",
        help=(
            "Measures the property's operating income relative "
            "to its purchase price, before mortgage financing."
        )
    )

with col3:

    st.metric(
        "Cash-on-Cash Return",
        f"{cash_on_cash_return:.2f}%",
        help=(
            "Measures annual cash flow compared with the cash "
            "initially invested in the property."
        )
    )

# ============================================================
# BREAK-EVEN ANALYSIS
# ============================================================

st.header("Break-Even Analysis")

st.write(
    "Break-even rent is the approximate monthly rent required "
    "for the property's rental income to cover its estimated "
    "operating expenses and mortgage payment."
)

break_even_data = pd.DataFrame(
    {
        "Monthly Rent": [
            break_even_monthly_rent * 0.70,
            break_even_monthly_rent * 0.80,
            break_even_monthly_rent * 0.90,
            break_even_monthly_rent,
            break_even_monthly_rent * 1.10,
            break_even_monthly_rent * 1.20,
            break_even_monthly_rent * 1.30
        ]
    }
)

break_even_data["Monthly Cash Flow"] = (
    break_even_data["Monthly Rent"]
    * (1 - vacancy_rate / 100)
    - total_operating_expenses / 12
    - monthly_mortgage_payment
)

break_even_chart = break_even_data.set_index("Monthly Rent")

st.line_chart(
    break_even_chart,
    y="Monthly Cash Flow",
    x_label="Monthly Rent ($)",
    y_label="Estimated Monthly Cash Flow ($)",
    width="stretch",
    height=350
)

st.caption(
    "The break-even point occurs where estimated monthly cash flow "
    "reaches approximately $0."
)

# ============================================================
# LONG-TERM WEALTH PROJECTION
# ============================================================

st.header("Potential Wealth Growth")

st.write(
    "This projection illustrates how property value, mortgage "
    "principal reduction and accumulated cash flow could affect "
    "your estimated equity over time."
)

st.warning(
    "Important: These are hypothetical scenarios, not forecasts. "
    "Actual property values, rents, expenses, interest rates and "
    "cash flow can be very different."
)

# ============================================================
# AMORTIZATION / WEALTH PROJECTION
# ============================================================

projection_rows = []

current_property_value = purchase_price
current_mortgage_balance = loan_amount
current_monthly_rent = monthly_rent
current_annual_expenses = total_operating_expenses
cumulative_cash_flow = 0

remaining_payments = number_of_payments

for year in range(1, projection_years + 1):

    beginning_balance = current_mortgage_balance

    annual_interest_paid = 0
    annual_principal_paid = 0
    annual_mortgage_paid = 0

    for month in range(12):

        if current_mortgage_balance <= 0:
            break

        interest_payment = (
            current_mortgage_balance
            * monthly_rate
        )

        principal_payment = (
            monthly_mortgage_payment
            - interest_payment
        )

        if principal_payment > current_mortgage_balance:
            principal_payment = current_mortgage_balance

        current_mortgage_balance -= principal_payment

        annual_interest_paid += interest_payment
        annual_principal_paid += principal_payment
        annual_mortgage_paid += (
            interest_payment + principal_payment
        )

    # Grow property value
    current_property_value *= (
        1 + appreciation_rate / 100
    )

    # Grow rent
    current_monthly_rent *= (
        1 + rent_growth_rate / 100
    )

    projected_annual_rent = (
        current_monthly_rent * 12
    )

    projected_vacancy_loss = (
        projected_annual_rent
        * vacancy_rate
        / 100
    )

    projected_income = (
        projected_annual_rent
        - projected_vacancy_loss
    )

    # Grow operating expenses
    current_annual_expenses *= (
        1 + expense_growth_rate / 100
    )

    projected_noi = (
        projected_income
        - current_annual_expenses
    )

    projected_cash_flow = (
        projected_noi
        - annual_mortgage_paid
    )

    cumulative_cash_flow += projected_cash_flow

    estimated_equity = (
        current_property_value
        - current_mortgage_balance
    )

    estimated_total_wealth = (
        estimated_equity
        + cumulative_cash_flow
    )

    projection_rows.append(
        {
            "Year": year,
            "Property Value": current_property_value,
            "Mortgage Balance": current_mortgage_balance,
            "Annual Principal Paid": annual_principal_paid,
            "Annual Interest Paid": annual_interest_paid,
            "Annual Cash Flow": projected_cash_flow,
            "Cumulative Cash Flow": cumulative_cash_flow,
            "Estimated Equity": estimated_equity,
            "Estimated Total Wealth": estimated_total_wealth
        }
    )

projection_df = pd.DataFrame(projection_rows)

# ============================================================
# WEALTH CHART
# ============================================================

st.subheader("Property Value, Mortgage & Equity")

wealth_chart_data = projection_df[
    [
        "Year",
        "Property Value",
        "Mortgage Balance",
        "Estimated Equity"
    ]
].set_index("Year")

st.line_chart(
    wealth_chart_data,
    width="stretch",
    height=400
)

st.caption(
    "Equity is estimated as property value minus remaining mortgage "
    "balance. The projection assumes the selected appreciation rate."
)

# ============================================================
# TOTAL WEALTH CHART
# ============================================================

st.subheader("Estimated Wealth Created Over Time")

total_wealth_chart = projection_df[
    [
        "Year",
        "Estimated Total Wealth"
    ]
].set_index("Year")

st.line_chart(
    total_wealth_chart,
    width="stretch",
    height=350
)

st.caption(
    "Estimated total wealth combines projected property equity "
    "and cumulative projected cash flow. It does not include "
    "taxes, selling costs, transaction costs or other investment returns."
)

# ============================================================
# PROJECTION SUMMARY
# ============================================================

st.subheader("Projection Summary")

final_year = projection_df.iloc[-1]

summary_col1, summary_col2 = st.columns(2)

with summary_col1:

    st.metric(
        f"Estimated Property Value — Year {projection_years}",
        f"${final_year['Property Value']:,.0f}"
    )

    st.metric(
        f"Estimated Equity — Year {projection_years}",
        f"${final_year['Estimated Equity']:,.0f}"
    )

with summary_col2:

    st.metric(
        f"Mortgage Balance — Year {projection_years}",
        f"${final_year['Mortgage Balance']:,.0f}"
    )

    st.metric(
        f"Cumulative Cash Flow — Year {projection_years}",
        f"${final_year['Cumulative Cash Flow']:,.0f}"
    )

# ============================================================
# EDUCATION: APPRECIATION VS DEPRECIATION
# ============================================================

st.header("Understanding Appreciation vs. Depreciation")

with st.expander("What is property appreciation?"):

    st.write(
        "Appreciation is an increase in the property's market value "
        "over time. For example, if a property purchased for $500,000 "
        "later becomes worth $550,000, the property has appreciated "
        "by $50,000."
    )

with st.expander("What is depreciation / CCA?"):

    st.write(
        "Depreciation is different from appreciation. In Canadian "
        "rental-property taxation, Capital Cost Allowance (CCA) can "
        "potentially allow an owner to claim a tax deduction for "
        "certain depreciable property."
    )

    st.write(
        "CCA is a tax concept and does not mean that the property's "
        "market value is falling."
    )

    st.write(
        "WTM. does not currently calculate CCA, tax savings or "
        "CCA recapture. Those should be handled as a separate "
        "Canadian tax-analysis module."
    )

with st.expander("Why doesn't WTM. include CCA in the wealth chart yet?"):

    st.write(
        "Because CCA affects taxes rather than the property's "
        "market value directly. Combining the two concepts could "
        "make the chart misleading."
    )

    st.write(
        "The current projection therefore focuses on three "
        "property-level wealth drivers:"
    )

    st.write(
        "1. Property appreciation\n\n"
        "2. Mortgage principal reduction\n\n"
        "3. Rental cash flow"
    )

# ============================================================
# DETAILED ANALYSIS
# ============================================================

st.header("Detailed Analysis")

with st.expander("View detailed calculations"):

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
        f"Monthly Mortgage Payment: "
        f"${monthly_mortgage_payment:,.0f}"
    )

    st.write(
        f"Annual Mortgage Payments: "
        f"${annual_mortgage_payments:,.0f}"
    )

    st.write(
        f"Annual Cash Flow: ${annual_cash_flow:,.0f}"
    )

    st.write(
        f"Monthly Cash Flow: ${monthly_cash_flow:,.0f}"
    )

    st.write(
        f"Cash-on-Cash Return: "
        f"{cash_on_cash_return:.2f}%"
    )

    st.write(
        f"Break-even Monthly Rent: "
        f"${break_even_monthly_rent:,.0f}"
    )

# ============================================================
# DISCLAIMER
# ============================================================

st.divider()

st.caption(
    "WTM. — Wealth That Matters"
)

st.caption(
    "This analysis is an estimate based on the information entered "
    "and is provided for educational and informational purposes only. "
    "It is not financial, investment, tax, legal, mortgage, or real "
    "estate advice. Actual results may differ materially. Users "
    "should independently verify all assumptions and consult "
    "qualified professionals before making financial decisions."
)
