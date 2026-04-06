name = "Igor"
country = "Sweden"
goal = 50000
current_income = 10000

progress = (current_income / goal) * 100

print("Привіт,", name)
print("Країна:", country)
print("Ціль по доходу:", goal, "euro")
print("Поточний дохід:", current_income, "euro")
print(f"Ти виконав {progress:.2f}% від своєї цілі")

if current_income >= goal:
    print("🎉 Вітаю! Ти досяг своєї цілі!")
else:
    remaining = goal - current_income
    print(f"⚡ Ти ще можеш заробити {remaining} euro, щоб досягти мети")
    
    # Savings forecast
profit = 6300
goal = 100000
remaining = goal - profit
months = remaining / profit
print(f"Months to 100k: {months:.1f}")

Add 100k savings forecast logic
