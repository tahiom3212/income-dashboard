goal = 70000
current = 10000

salary = 3500
expenses = 1000
it_income = 500

months = 0

while current < goal:
    monthly_save = salary - expenses + it_income
    current = current + monthly_save
    months = months + 1

    # IT grows every 3 months
    if months % 3 == 0:
        it_income = it_income + 100

print("🎯 Goal reached:", goal)
print("💶 Final amount:", current)
print("📅 Months:", months)
print("🗓️ Years:", round(months / 12, 1))
print("💻 Final IT income:", it_income)