import streamlit as st

# UI
st.title("💰 Personal Finance Tracker")
st.markdown("### 💡 Simple tool to understand your money flow")
st.write("Track your income, expenses, and see if you are saving money.")

# inputs
st.header("📊 Income")
income = st.number_input("💵 Monthly income (€)")

st.header("💸 Expenses")
rent = st.number_input("🏠 Rent (€)")
food = st.number_input("🍔 Food (€)")
other = st.number_input("📦 Other expenses (€)")
transport = st.number_input("🚗 Transport (€)")
gym = st.number_input("💪 Gym (€)")

# action
if st.button("Calculate"):
    st.divider()
    st.subheader("📈 Results")
    
    expenses = rent + food + other + transport + gym
    net = income - expenses

    col1, col2 = st.columns(2)

    with col1:
        st.metric("💸 Expenses", f"{expenses} €")

    with col2:
        st.metric("💵 Left", f"{net} €")

    # % витрат
    if income > 0:
        percent = (expenses / income) * 100
        st.write(f"📊 You spend {round(percent, 1)}% of your income")

    # статус + порада
    if net > 0:
        st.success(f"✅ You save {net} € per month")
        st.info("💡 Tip: You can increase your savings or invest.")
    elif net == 0:
        st.warning("⚖️ You break even")
        st.info("💡 Tip: Try to reduce small expenses.")
    else:
        st.error(f"❌ You lose {abs(net)} € per month")
        st.info("💡 Tip: Reduce expenses or increase income.")

    # графік
    st.subheader("📊 Expense Breakdown")
    st.bar_chart({
        "Rent": rent,
        "Food": food,
        "Other": other,
        "Transport": transport,
        "Gym": gym
    })
# reset
if st.button("Reset"):
    st.markdown(
        "<meta http-equiv='refresh' content='0'>",
        unsafe_allow_html=True
    )
    st.caption("Built with Python & Streamlit")