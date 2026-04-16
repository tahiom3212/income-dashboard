goal = float(input("Enter your goal: "))
current = float(input("Enter your current savings: "))
monthly = float(input("Enter monthly save: "))
side = float(input("Enter side income save: "))


def finance_summary(goal, current, monthly, side):
    total_monthly = monthly + side
    months = (goal - current) / total_monthly
    future = current + total_monthly * 12
    return months, future


print("Summary:", finance_summary(goal, current, monthly, side))