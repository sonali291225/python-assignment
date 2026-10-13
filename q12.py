attendance = [["Asha", 22, 2],["Rohan", 20, 4],["Neha", 24, 0]]

print(attendance[1][2])

attendance[1][2] = 3
attendance.append(["Sam", 21, 3])

total_present = 0

for row in attendance:
print(f"{row[0]}: present={row[1]}, absent={row[2]}")
total_present += row[1]

print("Total present:", total_present)
