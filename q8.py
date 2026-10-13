# Name: Sonali Banne

python_team = {"Asha", "Vikram", "Neha", "Ravi"}
sql_team = {"Neha", "Ravi", "Sam", "Tina", "Asha"}

print("Both:", sorted(python_team & sql_team))
print("At least one:", sorted(python_team | sql_team))
print("Only Python:", sorted(python_team - sql_team))
print("Only SQL:", sorted(sql_team - python_team))

python_team.add("Zoya")
python_team.remove("Vikram")

print("Python team:", sorted(python_team))

