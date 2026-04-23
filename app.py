import streamlit as st

# UI
st.title("💰Personal Finance Tracker")
st.write("Track your savings, expenses, and see if you are financially positive each month.")
st.caption("Simple tool to calculate your savings goal and timeline")

# inputs
st.header("📊 Income & Savings")

income = st.number_input("💵 Monthly income (€)")
savings = st.number_input("💰 Current savings (€)")

st.header("💸 Expenses")

rent = st.number_input("🏠 Rent (€)")
food = st.number_input("🍔 Food (€)")
other = st.number_input("📦 Other expenses (€)")

# logic
def finance_summary(goal, current, monthly, side):
    total = monthly + side
    if total == 0:
        return 0, current
    months = (goal - current) / total
    future = current + total * 12
    return months, future

# action
if st.button("Calculate"):
    total = monthly + side

    if total == 0:
        st.error("⚠️ Please enter monthly savings")

    elif goal <= current:
        st.success("🎉 You already reached your goal!")

    else:
        remaining = goal - current

        # 👇 expenses
        expenses = rent + food + other
    net = income - expenses

    st.write(f"💸 Total expenses: {expenses} €")
    st.write(f"💵 Money left: {net} €")

    if net > 0:
    st.success(f"✅ You save {net} € per month")
    else:
        st.error(f"❌ You lose {abs(net)} € per month")

        # 👇 основна логіка
        months, future = finance_summary(goal, current, monthly, side)

        st.write(f"💸 Remaining to save: {round(remaining, 2)} €")
        st.success(f"📅 You will reach your goal in {round(months, 1)} months")

        years = months / 12
        st.write(f"🗓️ That is about {round(years, 1)} years")

        if goal > 0:
            progress = (current / goal) * 100
            st.progress(min(int(progress), 100))
            st.write(f"📊 Progress: {round(progress, 1)}%")

        st.info(f"💰 In 12 months you will have: {round(future, 2)} €")

# reset
if st.button("Reset"):
    st.markdown(
        "<meta http-equiv='refresh' content='0'>",
        unsafe_allow_html=True
    )