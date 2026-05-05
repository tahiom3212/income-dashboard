import streamlit as st

# UI
st.title("🎯 Goal Calculator")
st.markdown("### 💡 How many days you need to reach your goal")

# inputs
hourly_rate = st.number_input("💶 Hourly rate (€)")
hours_per_day = st.number_input("⏱ Hours per day")
goal = st.number_input("🎯 Your goal (€)")