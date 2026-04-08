goal = 100000
current = 10000
months = 0

while current < goal:
    # Norway season: 8 months
    for i in range(8):
        forestry_income = 4500
        it_income = 300
        expenses = 1200

        current = current + forestry_income + it_income - expenses
        months = months + 1

        if current >= goal:
            break

    if current >= goal:
        break

    # Winter in Sweden: 4 months
    for i in range(4):
        it_income = 1200
        expenses = 1000

        current = current + it_income - expenses
        months = months + 1

        if current >= goal:
            break

print("🎯 Goal:", goal)
print("💶 Final:", current)
print("📅 Months:", months)
print("🗓️ Years:", round(months / 12, 1))