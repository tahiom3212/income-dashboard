goal = 70000
current = 10000
monthly = 2300


def savings_after_months(start, save, months):
    return start + save * months


def should_buy(price, monthly_save):
    return price / monthly_save


def monthly_goal_progress(goal, current, monthly):
    return (goal - current) / monthly


def finance_summary(goal, current, monthly):
    months = (goal - current) / monthly
    future = current + monthly * 6
    return months, future


print("Savings after 4 months:", savings_after_months(10000, 2000, 4))
print("Laptop delay:", should_buy(8000, 2000))
print("Months to 70k:", monthly_goal_progress(goal, current, monthly))
print("Finance summary:", finance_summary(goal, current, monthly))