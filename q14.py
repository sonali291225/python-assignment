# Name: Sonali Banne

salaries = [32000, 45000, 28000, 60000]

total_bonus = 0

for salary in salaries:
    bonus = salary * 0.08
    print(f"Salary: {salary} | Bonus: {bonus:.2f}")
    total_bonus += bonus

print(f"Total bonus: {total_bonus:.2f}")