import streamlit as st

st.title("🔥 TEST 123 🔥")

goal = st.number_input("Goal")
current = st.number_input("Current savings")
monthly = st.number_input("Monthly save")
side = st.number_input("Side income")


def finance_summary(goal, current, monthly, side):
    total = monthly + side
    if total == 0:
        return 0, current
    months = (goal - current) / total
    future = current + total * 12
    return months, future


if st.button("Calculate"):
    months, future = finance_summary(goal, current, monthly, side)
    st.write("Months to goal:", round(months, 2))
    st.write("Savings in 12 months:", future)