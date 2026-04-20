import streamlit as st

# UI
st.title("💰 Savings Goal Calculator")
st.caption("Simple tool to calculate your savings goal and timeline")

# inputs
goal = st.number_input("🎯 Your savings goal (€)")
current = st.number_input("💰 Current savings (€)")
monthly = st.number_input("💵 Monthly savings (€)")
side = st.number_input("⚡ Extra income (€)")

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
    else:
        remaining = goal - current
        st.write(f"💸 Remaining to save: {round(remaining, 2)} €")

        months, future = finance_summary(goal, current, monthly, side)

        st.success(f"📅 You will reach your goal in {round(months, 1)} months")
        st.info(f"💰 In 12 months you will have: {round(future, 2)} €")