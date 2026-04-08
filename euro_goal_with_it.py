goal = 70000
current = 10000

income = 3500
expenses = 1000

# Try different IT side income values
side_income = 500

monthly_save = income - expenses + side_income
remaining = goal - current
months = remaining / monthly_save

print("🎯 Goal:", goal, "EUR")
print("💶 Current:", current, "EUR")
print("💻 IT side income:", side_income, "EUR")
print("💾 Saved per month:", monthly_save, "EUR")
print(f"📅 Months to goal: {months:.1f}")
print(f"🗓️ Years to goal: {months / 12:.1f}")