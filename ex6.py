import streamlit as st

# ------------------------------------------
# PAGE CONFIG
# ------------------------------------------

st.set_page_config(
    page_title="💰 FinWise AI",
    page_icon="💰",
    layout="wide"
)

# ------------------------------------------
# CUSTOM CSS
# ------------------------------------------

st.markdown("""
<style>

.title{
text-align:center;
font-size:45px;
font-weight:bold;
color:#2E8B57;
}

.sub{
text-align:center;
font-size:18px;
color:gray;
}

div.stButton>button{
background:#2E8B57;
color:white;
font-size:18px;
height:50px;
width:100%;
border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# ------------------------------------------
# TITLE
# ------------------------------------------

st.markdown("<h1 class='title'>💰 FinWise AI</h1>", unsafe_allow_html=True)

st.markdown(
"<p class='sub'>Personal Finance Planner & Budget Tracker</p>",
unsafe_allow_html=True
)

st.write("")

# ------------------------------------------
# USER INPUTS
# ------------------------------------------

left, right = st.columns(2)

with left:

    name = st.text_input("👤 Enter Your Name")

    monthly_income = st.number_input(
        "💵 Monthly Income (₹)",
        min_value=0,
        value=30000,
        step=1000
    )

    savings_goal = st.number_input(
        "🎯 Monthly Savings Goal (₹)",
        min_value=0,
        value=10000,
        step=500
    )

with right:

    rent = st.number_input(
        "🏠 House Rent (₹)",
        min_value=0,
        value=5000,
        step=500
    )

    food = st.number_input(
        "🍛 Food Expenses (₹)",
        min_value=0,
        value=4000,
        step=500
    )

    travel = st.number_input(
        "🚌 Travel Expenses (₹)",
        min_value=0,
        value=2000,
        step=500
    )

    other = st.number_input(
        "🛒 Other Expenses (₹)",
        min_value=0,
        value=3000,
        step=500
    )

# ------------------------------------------
# BUTTON
# ------------------------------------------

analyze = st.button(
    "📊 Analyze My Finance",
    use_container_width=True
)
# ------------------------------------------
# FINANCE ANALYSIS
# ------------------------------------------

if analyze:

    if name.strip() == "":
        st.error("⚠ Please enter your name.")
        st.stop()

    # Calculations
    total_expenses = rent + food + travel + other
    savings = monthly_income - total_expenses

    if monthly_income > 0:
        expense_percentage = (total_expenses / monthly_income) * 100
        savings_percentage = (savings / monthly_income) * 100
    else:
        expense_percentage = 0
        savings_percentage = 0

    st.success(f"Welcome {name}! 👋")

    st.write("---")

    # ------------------------------------------
    # FINANCIAL SUMMARY
    # ------------------------------------------

    st.header("📊 Financial Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("💵 Income", f"₹{monthly_income}")

    with col2:
        st.metric("💸 Expenses", f"₹{total_expenses}")

    with col3:
        st.metric("🏦 Savings", f"₹{savings}")

    st.write("---")

    # ------------------------------------------
    # EXPENSE DETAILS
    # ------------------------------------------

    st.header("📋 Expense Details")

    st.write(f"🏠 Rent : ₹{rent}")
    st.write(f"🍛 Food : ₹{food}")
    st.write(f"🚌 Travel : ₹{travel}")
    st.write(f"🛒 Other : ₹{other}")

    st.write("---")

    # ------------------------------------------
    # SAVINGS GOAL
    # ------------------------------------------

    st.header("🎯 Savings Goal")

    if savings >= savings_goal:

        st.success("🎉 Congratulations! You achieved your monthly savings goal.")

    else:

        remaining = savings_goal - savings

        st.warning(f"You need to save ₹{remaining} more to reach your goal.")

    st.write("---")

    # ------------------------------------------
    # FINANCIAL HEALTH SCORE
    # ------------------------------------------

    st.header("⭐ Financial Health Score")

    if savings_percentage >= 30:
        score = 100

    elif savings_percentage >= 20:
        score = 90

    elif savings_percentage >= 10:
        score = 75

    elif savings_percentage >= 0:
        score = 60

    else:
        score = 40

    st.metric("Health Score", f"{score}/100")

    st.progress(score)
        # ------------------------------------------
    # MONEY SAVING TIPS
    # ------------------------------------------

    st.write("---")
    st.header("💡 Money Saving Tips")

    if rent > monthly_income * 0.40:
        st.warning("🏠 Your rent is more than 40% of your income.")

    if food > 6000:
        st.warning("🍛 Try cooking at home to reduce food expenses.")

    if travel > 3000:
        st.warning("🚌 Use public transport or carpool to save money.")

    if other > 5000:
        st.warning("🛒 Reduce unnecessary shopping and subscriptions.")

    if savings > 0:
        st.success("🏦 Great! Keep saving every month.")

    st.write("---")

    # ------------------------------------------
    # BUDGET ANALYSIS
    # ------------------------------------------

    st.header("📈 Budget Analysis")

    st.write(f"💸 Expense Percentage : **{expense_percentage:.1f}%**")
    st.write(f"🏦 Savings Percentage : **{savings_percentage:.1f}%**")

    if expense_percentage <= 50:
        st.success("Excellent! Your expenses are under control.")

    elif expense_percentage <= 70:
        st.info("Good! Try reducing unnecessary expenses.")

    else:
        st.error("Warning! Your expenses are too high.")

    st.write("---")

    # ------------------------------------------
    # EXPENSE BAR CHART
    # ------------------------------------------

    st.header("📊 Expense Comparison")

    chart_data = {

        "Amount":[

            rent,

            food,

            travel,

            other

        ]

    }

    st.bar_chart(chart_data)

    st.write("---")

    # ------------------------------------------
    # MONTHLY REPORT
    # ------------------------------------------

    st.header("📋 Monthly Finance Report")

    st.write(f"👤 Name : **{name}**")
    st.write(f"💵 Monthly Income : **₹{monthly_income}**")
    st.write(f"💸 Total Expenses : **₹{total_expenses}**")
    st.write(f"🏦 Savings : **₹{savings}**")
    st.write(f"🎯 Savings Goal : **₹{savings_goal}**")
    st.write(f"⭐ Financial Health Score : **{score}/100**")

    st.write("---")

    # ------------------------------------------
    # FINANCIAL STATUS
    # ------------------------------------------

    st.header("🏆 Financial Status")

    if score >= 90:

        st.success("🟢 Excellent Financial Health")

    elif score >= 75:

        st.success("🟡 Good Financial Health")

    elif score >= 60:

        st.warning("🟠 Average Financial Health")

    else:

        st.error("🔴 Poor Financial Health")
            # ------------------------------------------
    # PERSONALIZED SUGGESTIONS
    # ------------------------------------------

    st.write("---")
    st.header("🎯 Personalized Suggestions")

    if savings >= savings_goal:

        st.success("🎉 Congratulations! You achieved your savings goal.")

        st.write("✅ Continue investing regularly.")

        st.write("✅ Build an emergency fund.")

        st.write("✅ Start SIP or Mutual Fund investments.")

    else:

        st.warning("⚠ You haven't reached your savings goal.")

        st.write("💡 Reduce unnecessary expenses.")

        st.write("💡 Track every expense.")

        st.write("💡 Increase your monthly savings little by little.")

    # ------------------------------------------
    # SAVINGS PROGRESS
    # ------------------------------------------

    st.write("---")

    st.header("📈 Savings Progress")

    if savings_goal > 0:

        progress = min((savings / savings_goal) * 100, 100)

    else:

        progress = 0

    st.progress(progress / 100)

    st.write(f"Progress : **{progress:.1f}%**")

    # ------------------------------------------
    # FINANCIAL QUOTES
    # ------------------------------------------

    import random

    quotes = [

        "💰 Save money today for a better tomorrow.",

        "📈 Every rupee saved is a step toward financial freedom.",

        "🏦 Budget wisely and spend carefully.",

        "💡 Smart saving creates a secure future.",

        "🎯 Financial discipline leads to success."

    ]

    st.write("---")

    st.header("🔥 Financial Motivation")

    st.info(random.choice(quotes))

    # ------------------------------------------
    # FINAL SUMMARY
    # ------------------------------------------

    st.write("---")

    st.header("📑 Final Summary")

    st.success(f"""
👤 Name : {name}

💵 Monthly Income : ₹{monthly_income}

💸 Total Expenses : ₹{total_expenses}

🏦 Total Savings : ₹{savings}

⭐ Financial Health Score : {score}/100

🎯 Keep tracking your finances every month.
""")

    # ------------------------------------------
    # CELEBRATION
    # ------------------------------------------

    if score >= 90:

        st.balloons()

    # ------------------------------------------
    # FOOTER
    # ------------------------------------------

    st.write("---")

    st.caption(
        "💰 FinWise AI | Personal Finance Planner | Built using Python & Streamlit ❤️"
    )