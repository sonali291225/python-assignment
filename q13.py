# Name: Sonali Banne

departments = {
    "Analytics": {"head": "Meera", "budget": 500000, "team": 6},
    "Sales": {"head": "Karan", "budget": 750000, "team": 10},
    "HR": {"head": "Divya", "budget": 300000, "team": 3}
}

print(departments["Sales"]["head"])

departments["HR"]["budget"] += 50000

departments["IT"] = {
    "head": "Anil",
    "budget": 400000,
    "team": 5
}

total_budget = 0

for dept, details in departments.items():
    print(f"{dept} - head: {details['head']}, budget: {details['budget']}")
    total_budget += details["budget"]

print("Total budget:", total_budget)