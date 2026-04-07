goal = 1000000
saved = 0
monthly = 6300
months = 0

while saved < goal:
    saved = saved + monthly
    months = months + 1

    if months % 12 == 0:
        monthly = monthly * 1.10

print("Months:", months)
print("Years:", months / 12)
print("Saved:", round(saved, 2))