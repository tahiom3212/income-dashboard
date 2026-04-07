goal = 70000
current = 10000

# Slow scenario
income_low = 3000
expenses_high = 1500
monthly_save_low = income_low - expenses_high

# Fast scenario
income_high = 4000
expenses_low = 600
monthly_save_high = income_high - expenses_low

remaining = goal - current

months_slow = remaining / monthly_save_low
months_fast = remaining / monthly_save_high

print("🎯 Goal:", goal, "EUR")
print("💶 Current:", current, "EUR")
print()

print("🐢 Slow scenario")
print("Monthly saved:", monthly_save_low)
print(f"Months: {months_slow:.1f}")
print(f"Years: {months_slow / 12:.1f}")
print()

print("🚀 Fast scenario")
print("Monthly saved:", monthly_save_high)
print(f"Months: {months_fast:.1f}")
print(f"Years: {months_fast / 12:.1f}")