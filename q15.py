# Name: Sonali Banne

team = {
    "Asha": [24, 52000],
    "Rohan": [31, 61000],
    "Neha": [28, 47000]
}

total_payroll = 0

for name, details in team.items():
    age = details[0]
    salary = details[1]

    print(f"{name} is {age} years old and earns {salary}")
    total_payroll += salary

average_salary = total_payroll / len(team)

print("Total payroll:", total_payroll)
print(f"Average salary: {average_salary:.2f}")
print("Names:", sorted(team.keys()))