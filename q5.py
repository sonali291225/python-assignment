# Name: Sonali Banne

# Take the total hours worked in a week
hours_worked = int(input("Hours worked: "))

# Calculate standard weekly hours
standard_hours = 40

# Calculate overtime hours
overtime_hours = hours_worked - standard_hours

# Calculate overtime pay at Rs. 300 per hour
overtime_pay = overtime_hours * 300

# Print the overtime details
print("Hours worked:", hours_worked)
print("Overtime hours:", overtime_hours)
print("Overtime pay:", overtime_pay)