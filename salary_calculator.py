import streamlit as st

# UI
st.title("💸 Salary Calculator")
st.markdown("### 💡 Calculate your earnings based on hourly work")

# inputs
hourly_rate = st.number_input("💶 Hourly rate (€)")
hours_per_day = st.number_input("⏱ Hours per day")
days_worked = st.number_input("📅 Days worked")
extra_days = st.number_input("📅 Extra days (plan ahead)")

# action
if st.button("Calculate"):
    st.divider()
    st.subheader("📊 Results")

    # розрахунки
    daily_income = hourly_rate * hours_per_day
    total_income = daily_income * days_worked
    monthly_income = daily_income * 20
    future_income = daily_income * extra_days

    # основні результати
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("💰 Daily", f"{daily_income} €")

    with col2:
        st.metric("💰 Total", f"{total_income} €")

    with col3:
        st.metric("📅 Month (est.)", f"{monthly_income} €")

    # планування 
    st.subheader("🔮 Planning")
    st.metric("Future earnings", f"{future_income} €")
# reset
if st.button("Reset"):
    st.markdown(
        "<meta http-equiv='refresh' content='0'>",
        unsafe_allow_html=True
    )

st.caption("Built with Python & Streamlit")