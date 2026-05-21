import streamlit as st

# UI
st.title("🎯 Goal Calculator")
st.markdown("### 💡 How many days you need to reach your goal")

# inputs
hourly_rate = st.number_input("💶 Hourly rate (€)")
hours_per_day = st.number_input("⏱ Hours per day")
goal = st.number_input("🎯 Your goal (€)")

# action
if st.button("Calculate"):

    daily_income = hourly_rate * hours_per_day

    if daily_income > 0:
        days_needed = goal / daily_income

        st.divider()
        st.subheader("📊 Results")

        st.metric("💰 Daily income", f"{daily_income} €")
        st.metric("🎯 Days needed", f"{round(days_needed, 1)}")

    else:
        st.warning("⚠️ Enter hourly rate and hours")