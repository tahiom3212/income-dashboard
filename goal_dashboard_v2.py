goal = float(input("Enter your goal: "))
current = float(input("Enter your current savings: "))
monthly = float(input("Enter monthly save: "))


def finance_summary(goal, current, monthly):
    months = (goal - current) / monthly
    future = current + monthly * 6
    return months, future


print("Summary:", finance_summary(goal, current, monthly))