import streamlit as st

# UI
st.title("💰 Personal Finance Tracker")
st.write("Track your income, expenses, and see if you are saving money.")

# inputs
st.header("📊 Income")

income = st.number_input("💵 Monthly income (€)")

st.header("💸 Expenses")

rent = st.number_input("🏠 Rent (€)")
food = st.number_input("🍔 Food (€)")
other = st.number_input("📦 Other expenses (€)")
transport = st.number_input("🚗 Transport (€)")

# action
if st.button("Calculate"):
    expenses = rent + food + other + transport
    net = income - expenses

    st.write(f"💸 Total expenses: {expenses} €")
    st.write(f"💵 Money left: {net} €")

    if net > 0:
        st.success(f"✅ You save {net} € per month")
    elif net == 0:
        st.warning("⚖️ You break even")
    else:
        st.error(f"❌ You lose {abs(net)} € per month")

# reset
if st.button("Reset"):
    st.markdown(
        "<meta http-equiv='refresh' content='0'>",
        unsafe_allow_html=True
    )