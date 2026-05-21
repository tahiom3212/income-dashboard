import streamlit as st

# UI
st.title("🎯 Goal Calculator")
st.markdown("### 💡 How many days you need to reach your goal")

# inputs
hourly_rate = st.number_input("💶 Hourly rate (€)")
hours_per_day = st.number_input("⏱ Hours per day")
goal = st.number_input("🎯 Your goal (€)")
working_days_week = st.number_input(
    "📅 Working days per week",
    min_value=1,
    max_value=7,
    value=5
)

# action
if st.button("Calculate"):

    daily_income = hourly_rate * hours_per_day

    if daily_income > 0:
        days_needed = goal / daily_income
        weeks_needed = days_needed / working_days_week
        months_needed = weeks_needed / 4.3
        
        st.divider()
        st.subheader("📊 Results")

        st.metric("💰 Daily income", f"{daily_income} €")
        st.metric("🎯 Days needed", f"{round(days_needed, 1)}")
        
        st.metric("📅 Weeks (est.)", f"{round(weeks_needed, 1)}")
        st.metric("🗓 Months (est.)", f"{round(months_needed, 1)}")

        st.info(
            f"💡 To reach {goal} €, you need about "
            f"{round(days_needed,1)} working days."
)
    
    else:
        st.warning("⚠️ Enter hourly rate and hours")