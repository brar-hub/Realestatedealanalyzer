import streamlit as st
import pandas as pd
import numpy as np


# ============================================================
# WTM. — WEALTH THAT MATTERS
# REAL ESTATE DEAL ANALYZER
# ============================================================

st.set_page_config(
    page_title="WTM. Real Estate Deal Analyzer",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ========================================================
       GENERAL PAGE
       ======================================================== */

    .block-container {
        max-width: 1400px;
        padding-top: 2rem;
        padding-left: 4%;
        padding-right: 4%;
        padding-bottom: 4rem;
    }


    /* ========================================================
       CENTERED WTM HEADER
       ======================================================== */

    .wtm-header {
        text-align: center;
        width: 100%;
        margin-bottom: 30px;
    }

    .wtm-brand {
        font-size: clamp(44px, 6vw, 72px);
        font-weight: 800;
        letter-spacing: -2px;
        line-height: 1;
        margin-bottom: 8px;
    }

    .wtm-tagline {
        font-size: clamp(16px, 2vw, 21px);
        font-weight: 500;
        margin-bottom: 18px;
    }

    .app-title {
        font-size: clamp(28px, 4vw, 42px);
        font-weight: 750;
        margin-top: 10px;
        margin-bottom: 10px;
    }

    .app-description {
        font-size: clamp(15px, 1.7vw, 18px);
        max-width: 850px;
        margin: 0 auto 30px auto;
        line-height: 1.6;
        opacity: 0.85;
    }


    /* ========================================================
       SECTION TITLES
       ======================================================== */

    .section-title {
        font-size: clamp(21px, 2.5vw, 27px);
        font-weight: 700;
        margin-top: 28px;
        margin-bottom: 14px;
    }


    /* ========================================================
       ANALYSIS
       ======================================================== */

    .analysis-card {
        padding: 20px;
        border-radius: 12px;
        border: 1px solid rgba(128,128,128,0.25);
        margin-bottom: 15px;
    }

    .health-good,
    .health-marginal,
    .health-poor {
        font-size: clamp(22px, 3vw, 28px);
        font-weight: 700;
        margin-bottom: 15px;
    }

    .metric-label {
        font-size: 14px;
        opacity: 0.75;
    }

    .metric-value {
        font-size: 25px;
        font-weight: 700;
    }


    /* ========================================================
       WATERMARK
       ======================================================== */

    .watermark {
        display: none;
    }


    /* ========================================================
       DISCLAIMER
       ======================================================== */

    .disclaimer {
        font-size: 12px;
        opacity: 0.7;
        margin-top: 35px;
        padding-top: 18px;
        border-top: 1px solid rgba(128,128,128,0.25);
        line-height: 1.6;
    }


    /* ========================================================
       RESPONSIVE DESIGN
       ======================================================== */

    @media screen and (max-width: 900px) {

        .block-container {
            padding-left: 3%;
            padding-right: 3%;
            padding-top: 1.25rem;
        }

        .section-title {
            margin-top: 22px;
        }
    }


    @media screen and (max-width: 600px) {

        .block-container {
            padding-left: 18px;
            padding-right: 18px;
        }

        .wtm-header {
            margin-bottom: 20px;
        }

        .app-description {
            margin-bottom: 20px;
        }

        .section-title {
            margin-top: 20px;
        }
    }


    /* ========================================================
       PRINT
       ======================================================== */

    @media print {

        @page {
            size: auto;
            margin: 0.55in;
        }

        body {
            -webkit-print-color-adjust: exact;
            print-color-adjust: exact;
        }

        .stApp {
            position: relative;
        }

        .watermark {
            display: block !important;
            position: fixed;
            top: 45%;
            left: 50%;
            transform: translate(-50%, -50%) rotate(-25deg);
            font-size: 100px;
            font-weight: 800;
            opacity: 0.07;
            z-index: 9999;
            pointer-events: none;
        }

        button,
        [data-testid="stSidebar"],
        [data-testid="stHeader"],
        [data-testid="stToolbar"] {
            display: none !important;
        }

        .no-print {
            display: none !important;
        }

        .block-container {
            max-width: none;
            padding: 0;
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# PRINT WATERMARK
# ============================================================

st.markdown(
    '<div class="watermark">WTM.</div>',
    unsafe_allow_html=True
)


# ============================================================
# HEADER
# ============================================================

header_left, header_middle, header_right = st.columns([1, 2, 1])

with header_middle:

    st.markdown(
        """
        <div class="wtm-header">

            <div class="wtm-brand">
                WTM.
            </div>

            <div class="wtm-tagline">
                Wealth That Matters
            </div>

            <div class="app-title">
                Real Estate Deal Analyzer
            </div>

            <div class="app-description">
                A free tool to analyze real estate investment opportunities
                and understand how a property could build wealth over time.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# PRINT BUTTON
# ============================================================

with header_right:

    st.markdown(
        '<div class="no-print" style="margin-top:10px;">',
        unsafe_allow_html=True
    )

    if st.button(
        "🖨️ Print",
        use_container_width=True,
        help="Print the analysis or save it as a PDF using your browser's print dialog."
    ):
        st.markdown(
            """
            <script>
                window.print();
            </script>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# PROPERTY INFORMATION
# ============================================================

st.markdown(
    '<div class="section-title">Property Information</div>',
    unsafe_allow_html=True
)


# Responsive Streamlit columns
col1, col2 = st.columns(2)


with col1:

    purchase_price = st.number_input(
        "Purchase Price ($)",
        min_value=0.0,
        value=500000.0,
        step=5000.0,
        format="%.0f",
        help="""
        The price you expect to pay for the property before financing,
        closing costs, renovations, or other acquisition costs.
        """
    )

    monthly_rent = st.number_input(
        "Monthly Rent ($)",
        min_value=0.0,
        value=3000.0,
        step=100.0,
        format="%.0f",
        help="""
        The total rent you expect to collect each month if the property
        is fully occupied.
        """
    )

    down_payment = st.number_input(
        "Down Payment ($)",
        min_value=0.0,
        value=100000.0,
        step=5000.0,
        format="%.0f",
        help="""
        The amount of your own money invested into the property at purchase.
        A larger down payment generally reduces the mortgage but increases
        the amount of capital tied up in the property.
        """
    )


with col2:

    interest_rate = st.number_input(
        "Mortgage Interest Rate (%)",
        min_value=0.0,
        max_value=30.0,
        value=5.14,
        step=0.05,
        format="%.2f",
        help="""
        The annual interest rate charged on the mortgage.
        This affects your monthly mortgage payment and investment cash flow.
        """
    )

    amortization_years = st.number_input(
        "Amortization (Years)",
        min_value=1,
        max_value=50,
        value=25,
        step=1,
        help="""
        The number of years used to calculate the mortgage payment.
        A longer amortization generally lowers the monthly payment but
        increases total interest paid over the life of the loan.
        """
    )


# ============================================================
# OPERATING EXPENSES
# ============================================================

st.markdown(
    '<div class="section-title">Operating Expenses</div>',
    unsafe_allow_html=True
)


col1, col2 = st.columns(2)


with col1:

    property_tax = st.number_input(
        "Annual Property Tax ($)",
        min_value=0.0,
        value=4000.0,
        step=250.0,
        format="%.0f",
        help="""
        The annual property tax charged by the municipality.

        Property tax is an operating expense and reduces the income
        generated by the property.
        """
    )

    insurance = st.number_input(
        "Annual Insurance ($)",
        min_value=0.0,
        value=1500.0,
        step=100.0,
        format="%.0f",
        help="""
        Estimated annual property insurance cost.
        """
    )


with col2:

    maintenance = st.number_input(
        "Annual Maintenance ($)",
        min_value=0.0,
        value=3000.0,
        step=250.0,
        format="%.0f",
        help="""
        Estimated annual repairs and maintenance.

        This may include routine repairs, replacement items,
        landscaping, appliance repairs, and similar costs.
        """
    )

    vacancy_rate = st.number_input(
        "Vacancy Rate (%)",
        min_value=0.0,
        max_value=100.0,
        value=5.0,
        step=0.5,
        format="%.1f",
        help="""
        Vacancy rate estimates the percentage of potential rental income
        that may be lost because the property is empty or between tenants.

        Example:
        A 5% vacancy rate means the analysis assumes approximately
        5% of annual potential rent will not be collected.

        Basic calculation:
        Vacancy Loss = Annual Gross Rent × Vacancy Rate
        """
    )


# ============================================================
# LONG-TERM ASSUMPTIONS
# ============================================================

st.markdown(
    '<div class="section-title">Long-Term Wealth Assumptions</div>',
    unsafe_allow_html=True
)


col1, col2, col3 = st.columns(3)


with col1:

    appreciation_rate = st.number_input(
        "Annual Property Appreciation (%)",
        min_value=-20.0,
        max_value=30.0,
        value=3.0,
        step=0.5,
        format="%.1f",
        help="""
        Assumed annual increase or decrease in the property's market value.

        This is a scenario assumption, not a prediction.
        """
    )


with col2:

    rent_growth_rate = st.number_input(
        "Annual Rent Growth (%)",
        min_value=-20.0,
        max_value=30.0,
        value=2.5,
        step=0.5,
        format="%.1f",
        help="""
        Assumed annual growth in rental income.

        This is a scenario assumption and actual rent growth depends
        on market conditions and applicable regulations.
        """
    )


with col3:

    depreciation_rate = st.number_input(
        "Illustrative Depreciation (%)",
        min_value=0.0,
        max_value=20.0,
        value=4.0,
        step=0.5,
        format="%.1f",
        help="""
        An illustrative annual depreciation rate used only to visualize
        how a property's depreciable value could decline over time.

        Actual tax depreciation rules are jurisdiction-specific and may
        differ substantially from this simplified illustration.
        """
    )


# ============================================================
# CALCULATIONS
# ============================================================

annual_gross_rent = monthly_rent * 12

vacancy_loss = annual_gross_rent * (vacancy_rate / 100)

effective_gross_income = annual_gross_rent - vacancy_loss

operating_expenses = (
    property_tax
    + insurance
    + maintenance
)

noi = effective_gross_income - operating_expenses

cap_rate = (
    noi / purchase_price * 100
    if purchase_price > 0
    else 0
)

loan_amount = max(
    purchase_price - down_payment,
    0
)

monthly_rate = interest_rate / 100 / 12

number_of_payments = amortization_years * 12


if loan_amount <= 0:

    monthly_mortgage_payment = 0

elif monthly_rate == 0:

    monthly_mortgage_payment = (
        loan_amount / number_of_payments
    )

else:

    monthly_mortgage_payment = (
        loan_amount
        * (
            monthly_rate
            * (1 + monthly_rate) ** number_of_payments
        )
        / (
            (1 + monthly_rate) ** number_of_payments - 1
        )
    )


annual_mortgage_payments = (
    monthly_mortgage_payment * 12
)

annual_cash_flow = (
    noi - annual_mortgage_payments
)

monthly_cash_flow = (
    annual_cash_flow / 12
)

cash_invested = down_payment

cash_on_cash_return = (
    annual_cash_flow / cash_invested * 100
    if cash_invested > 0
    else 0
)


# ============================================================
# BREAK-EVEN RENT
# ============================================================

annual_break_even_rent = (
    (
        operating_expenses
        + annual_mortgage_payments
    )
    / (1 - vacancy_rate / 100)
    if vacancy_rate < 100
    else 0
)

break_even_monthly_rent = (
    annual_break_even_rent / 12
)


# ============================================================
# DEAL HEALTH
# ============================================================

if monthly_cash_flow >= 300:

    health = "🟢 Strong"
    health_class = "health-good"

elif monthly_cash_flow >= 0:

    health = "🟡 Marginal"
    health_class = "health-marginal"

else:

    health = "🔴 Negative"
    health_class = "health-poor"


# ============================================================
# QUICK DEAL ANALYSIS
# ============================================================

st.markdown(
    '<div class="section-title">Quick Deal Analysis</div>',
    unsafe_allow_html=True
)

st.markdown(
    f'<div class="{health_class}">Deal Health: {health}</div>',
    unsafe_allow_html=True
)


if monthly_cash_flow > 0:

    deal_summary = f"""
    This property is estimated to generate approximately
    **${monthly_cash_flow:,.0f} per month in positive cash flow**
    after estimated operating expenses and mortgage payments.
    """

elif monthly_cash_flow < 0:

    deal_summary = f"""
    This property is estimated to require approximately
    **${abs(monthly_cash_flow):,.0f} per month from the investor**
    after estimated operating expenses and mortgage payments.
    """

else:

    deal_summary = """
    This property is estimated to approximately break even each month
    after the assumptions entered above.
    """


st.markdown(deal_summary)


st.markdown(
    f"""
    At the current assumptions, the property generates a
    **{cap_rate:.2f}% cap rate** and a
    **{cash_on_cash_return:.2f}% cash-on-cash return**.

    The estimated break-even rent is approximately
    **${break_even_monthly_rent:,.0f} per month**.
    """
)


# ============================================================
# PLAIN ENGLISH INTERPRETATION
# ============================================================

if monthly_cash_flow > 0 and cash_on_cash_return >= 5:

    interpretation = """
    **What this means:** The property is currently producing positive cash
    flow and the amount of cash invested is generating a reasonable annual
    return under these assumptions. The investment may have a solid starting
    position, but the purchase price, financing, property condition and
    future expenses still matter.
    """

elif monthly_cash_flow > 0:

    interpretation = """
    **What this means:** The property is currently paying its estimated
    operating costs and mortgage and still leaves some cash flow for the
    investor. However, the return on the cash invested is relatively modest,
    so the investment may depend more heavily on long-term equity growth,
    rent growth or appreciation.
    """

else:

    interpretation = """
    **What this means:** The property's current rental income does not fully
    cover the estimated expenses and mortgage payment. An investor would
    need to contribute additional cash each month unless the assumptions
    change through a lower purchase price, higher rent, lower expenses,
    different financing or another strategy.
    """


st.info(interpretation)


# ============================================================
# KEY METRICS
# ============================================================

m1, m2, m3, m4 = st.columns(4)


with m1:

    st.metric(
        "Monthly Cash Flow",
        f"${monthly_cash_flow:,.0f}"
    )


with m2:

    st.metric(
        "Cap Rate",
        f"{cap_rate:.2f}%"
    )


with m3:

    st.metric(
        "Cash-on-Cash",
        f"{cash_on_cash_return:.2f}%"
    )


with m4:

    st.metric(
        "Break-Even Rent",
        f"${break_even_monthly_rent:,.0f}"
    )


# ============================================================
# DETAILED ANALYSIS
# ============================================================

st.markdown(
    '<div class="section-title">Detailed Analysis</div>',
    unsafe_allow_html=True
)


d1, d2 = st.columns(2)


with d1:

    st.write(
        f"**Annual Gross Rent:** ${annual_gross_rent:,.0f}"
    )

    st.write(
        f"**Vacancy Loss:** ${vacancy_loss:,.0f}"
    )

    st.write(
        f"**Effective Gross Income:** "
        f"${effective_gross_income:,.0f}"
    )

    st.write(
        f"**Operating Expenses:** "
        f"${operating_expenses:,.0f}"
    )

    st.write(
        f"**Net Operating Income:** ${noi:,.0f}"
    )

    st.write(
        f"**Cap Rate:** {cap_rate:.2f}%"
    )


with d2:

    st.write(
        f"**Loan Amount:** ${loan_amount:,.0f}"
    )

    st.write(
        f"**Monthly Mortgage Payment:** "
        f"${monthly_mortgage_payment:,.0f}"
    )

    st.write(
        f"**Annual Mortgage Payments:** "
        f"${annual_mortgage_payments:,.0f}"
    )

    st.write(
        f"**Annual Cash Flow:** "
        f"${annual_cash_flow:,.0f}"
    )

    st.write(
        f"**Monthly Cash Flow:** "
        f"${monthly_cash_flow:,.0f}"
    )

    st.write(
        f"**Cash-on-Cash Return:** "
        f"{cash_on_cash_return:.2f}%"
    )


# ============================================================
# BREAK-EVEN ANALYSIS
# ============================================================

st.markdown(
    '<div class="section-title">Break-Even Analysis</div>',
    unsafe_allow_html=True
)


st.write(
    f"""
    The estimated break-even rent is
    **${break_even_monthly_rent:,.0f}/month**.

    This means the property would need approximately this level of monthly
    rent, under the assumptions entered, for rental income to cover estimated
    operating expenses and mortgage payments.
    """
)


rent_range = np.linspace(
    max(0, monthly_rent * 0.5),
    max(
        monthly_rent * 1.5,
        break_even_monthly_rent * 1.25
    ),
    100
)


cash_flow_range = []


for rent in rent_range:

    gross = rent * 12

    vacancy = (
        gross * vacancy_rate / 100
    )

    effective_income = (
        gross - vacancy
    )

    cash_flow = (
        effective_income
        - operating_expenses
        - annual_mortgage_payments
    )

    cash_flow_range.append(
        cash_flow / 12
    )


break_even_df = pd.DataFrame(
    {
        "Monthly Rent": rent_range,
        "Monthly Cash Flow": cash_flow_range
    }
)


st.line_chart(
    break_even_df.set_index("Monthly Rent"),
    y="Monthly Cash Flow"
)


st.caption(
    "The point where the line crosses $0 represents the approximate "
    "monthly rent required to break even."
)


# ============================================================
# LONG-TERM WEALTH MODEL
# ============================================================

st.markdown(
    '<div class="section-title">Long-Term Wealth & Equity Scenario</div>',
    unsafe_allow_html=True
)


st.write(
    """
    This section illustrates how the property could build equity over time
    through three major components:

    **1. Property appreciation** — potential increase in market value.

    **2. Mortgage principal reduction** — part of each mortgage payment
    reduces the loan balance.

    **3. Rental cash flow** — income remaining after estimated expenses
    and mortgage payments.

    These are scenario estimates, not predictions.
    """
)


# ============================================================
# AMORTIZATION / PROPERTY VALUE MODEL
# ============================================================

years = list(
    range(
        0,
        amortization_years + 1
    )
)


balance = loan_amount

rows = []

cumulative_cash_flow = 0


for year in years:

    if year == 0:

        current_balance = loan_amount

        current_property_value = purchase_price

        cumulative_cash_flow = 0

    else:

        for month in range(12):

            if balance <= 0:

                balance = 0

                break

            interest_payment = (
                balance * monthly_rate
            )

            principal_payment = (
                monthly_mortgage_payment
                - interest_payment
            )

            principal_payment = max(
                principal_payment,
                0
            )

            balance -= principal_payment

            balance = max(
                balance,
                0
            )

        current_balance = balance

        current_property_value = (
            purchase_price
            * (
                1 + appreciation_rate / 100
            ) ** year
        )

        cumulative_cash_flow += (
            annual_cash_flow
        )

    equity = (
        current_property_value
        - current_balance
    )

    rows.append(
        {
            "Year": year,
            "Property Value": current_property_value,
            "Mortgage Balance": current_balance,
            "Property Equity": equity,
            "Cumulative Cash Flow": cumulative_cash_flow
        }
    )


wealth_df = pd.DataFrame(rows)


# ============================================================
# WEALTH CHART
# ============================================================

st.markdown(
    "### Property Value vs. Mortgage Balance"
)


chart_df = wealth_df.set_index(
    "Year"
)[
    [
        "Property Value",
        "Mortgage Balance",
        "Property Equity"
    ]
]


st.line_chart(chart_df)


st.caption(
    "The chart illustrates the relationship between estimated property value, "
    "remaining mortgage balance and accumulated equity."
)


# ============================================================
# EQUITY SUMMARY
# ============================================================

final_row = wealth_df.iloc[-1]


final_property_value = (
    final_row["Property Value"]
)

final_mortgage_balance = (
    final_row["Mortgage Balance"]
)

final_equity = (
    final_row["Property Equity"]
)


e1, e2, e3 = st.columns(3)


with e1:

    st.metric(
        f"Estimated Property Value — "
        f"Year {amortization_years}",
        f"${final_property_value:,.0f}"
    )


with e2:

    st.metric(
        f"Estimated Mortgage Balance — "
        f"Year {amortization_years}",
        f"${final_mortgage_balance:,.0f}"
    )


with e3:

    st.metric(
        f"Estimated Equity — "
        f"Year {amortization_years}",
        f"${final_equity:,.0f}"
    )


# ============================================================
# DEPRECIATION ILLUSTRATION
# ============================================================

st.markdown(
    '<div class="section-title">Illustrative Depreciation Scenario</div>',
    unsafe_allow_html=True
)


st.warning(
    """
    **Important:** This is an educational visualization only.

    Tax depreciation is not the same thing as a property's market value
    declining. Actual tax treatment depends on the property, jurisdiction,
    ownership structure, tax rules and eligible depreciable assets.

    Consult a qualified tax professional before using depreciation for
    tax planning.
    """
)


depreciation_rows = []


depreciable_basis = purchase_price


for year in range(
    0,
    amortization_years + 1
):

    remaining_value = (
        depreciable_basis
        * (
            1 - depreciation_rate / 100
        ) ** year
    )

    depreciation_rows.append(
        {
            "Year": year,
            "Illustrative Remaining Depreciable Value":
                remaining_value
        }
    )


depreciation_df = pd.DataFrame(
    depreciation_rows
).set_index(
    "Year"
)


st.line_chart(
    depreciation_df
)


st.caption(
    "This simplified curve demonstrates how a depreciable basis could decline "
    "under the selected illustrative rate. It does not calculate a tax claim."
)


# ============================================================
# RENT GROWTH SCENARIO
# ============================================================

st.markdown(
    '<div class="section-title">Potential Rental Income Growth</div>',
    unsafe_allow_html=True
)


rent_rows = []


for year in range(
    0,
    amortization_years + 1
):

    projected_monthly_rent = (
        monthly_rent
        * (
            1 + rent_growth_rate / 100
        ) ** year
    )

    rent_rows.append(
        {
            "Year": year,
            "Projected Monthly Rent":
                projected_monthly_rent
        }
    )


rent_df = pd.DataFrame(
    rent_rows
).set_index(
    "Year"
)


st.line_chart(
    rent_df
)


st.caption(
    "This is a scenario based on the rent-growth assumption entered above."
)


# ============================================================
# INVESTOR TAKEAWAY
# ============================================================

st.markdown(
    '<div class="section-title">Investor Takeaway</div>',
    unsafe_allow_html=True
)


if monthly_cash_flow > 0:

    cashflow_sentence = (
        f"The property is currently estimated to produce about "
        f"${monthly_cash_flow:,.0f} per month after the assumptions entered."
    )

else:

    cashflow_sentence = (
        f"The property is currently estimated to have a monthly shortfall "
        f"of approximately ${abs(monthly_cash_flow):,.0f}."
    )


st.markdown(
    f"""
    **In simple terms:**

    {cashflow_sentence}

    The property's estimated **{cap_rate:.2f}% cap rate** helps describe
    the property's operating income relative to its purchase price.

    The **{cash_on_cash_return:.2f}% cash-on-cash return** looks at the
    annual cash flow relative to the cash invested.

    The estimated break-even rent is
    **${break_even_monthly_rent:,.0f} per month**, which gives the investor
    a useful target when comparing the property's current rent with its
    required income.

    Over the long term, the property may also build wealth through mortgage
    principal reduction, property appreciation and potential rental growth.
    However, these outcomes are uncertain and depend on actual market
    conditions.
    """
)


# ============================================================
# EDUCATIONAL DEFINITIONS
# ============================================================

with st.expander(
    "📘 Simple Definitions — Key Terms"
):

    st.markdown(
        """
        **Cap Rate**

        A quick way to compare a property's operating income with its price.

        **Formula:** Net Operating Income ÷ Property Value/Purchase Price.

        Higher does not automatically mean better. A higher cap rate may
        come with higher risk, weaker locations, older properties or other
        trade-offs.


        **Cash-on-Cash Return**

        Measures the annual cash flow generated compared with the cash
        you personally invested.

        Example: If you invested $100,000 and received $5,000 in annual
        cash flow, the cash-on-cash return would be 5%.


        **Net Operating Income (NOI)**

        The property's income after normal operating expenses but before
        mortgage payments and income taxes.


        **Vacancy Rate**

        An estimate of the percentage of potential rental income that may
        be lost because the property is empty or between tenants.

        Example: A 5% vacancy rate means the model assumes approximately
        5% of potential annual rent will not be collected.


        **Cash Flow**

        The money left after rental income, operating expenses and mortgage
        payments.


        **Break-Even Rent**

        The approximate monthly rent required for the property's rental
        income to cover its estimated operating expenses and mortgage.


        **Equity**

        The portion of the property that belongs to the owner after
        subtracting the outstanding mortgage from the property's estimated
        market value.


        **Appreciation**

        An increase in the market value of the property over time.


        **Depreciation**

        A reduction in the value assigned to an asset for accounting or
        tax purposes. It does not necessarily mean the property's market
        value is falling.
        """
    )


# ============================================================
# DISCLAIMER
# ============================================================

st.markdown(
    """
    <div class="disclaimer">

    <strong>Disclaimer</strong><br><br>

    WTM. Real Estate Deal Analyzer is provided for educational and
    informational purposes only. The calculations are estimates based on
    the assumptions entered by the user and should not be considered
    financial, investment, tax, accounting, legal, mortgage or real estate
    advice.

    Actual results may differ materially due to financing terms, taxes,
    insurance, maintenance, vacancy, rent changes, property condition,
    market conditions, transaction costs, regulations and other factors.

    The depreciation section is an illustrative scenario and does not
    calculate or recommend a tax deduction.

    Users should independently verify all assumptions and consult
    appropriately qualified professionals before making investment or
    financial decisions.

    <br><br>

    <strong>WTM. — Wealth That Matters</strong>

    </div>
    """,
    unsafe_allow_html=True
)
