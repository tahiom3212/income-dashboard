import streamlit as st

# UI
st.title("💰 Savings Goal Calculator")
st.caption("Simple tool to calculate your savings goal and timeline")

# inputs
goal = st.number_input("🎯 Your savings goal (€)", key="goal")
current = st.number_input("💰 Current savings (€)", key="current")
monthly = st.number_input("💵 Monthly savings (€)", key="monthly")
side = st.number_input("⚡ Extra income (€)", key="side")
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
        months, future = finance_summary(goal, current, monthly, side)

        st.write(f"💸 Remaining to save: {round(remaining, 2)} €")

        st.success(f"📅 You will reach your goal in {round(months, 1)} months")

        # (роки)
        years = months / 12
        st.write(f"🗓️ That is about {round(years, 1)} years")

        # (прогрес)
        if goal > 0:
            progress = (current / goal) * 100
            st.write(f"📊 Progress: {round(progress, 1)}%")

        st.info(f"💰 In 12 months you will have: {round(future, 2)} €")

# 👇
if st.button("Reset"):
    st.session_state.goal = 0
    st.session_state.current = 0
    st.session_state.monthly = 0
    st.session_state.side = 0
    st.rerun()