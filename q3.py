hours_per_day =float(input("Hours per day: ").strip())
working_days = int(input("Working days:"))
hourly_rate = float(input("Hourly rate:"))

total_hours = hours_per_day * working_days
total_pay = total_hours * hourly_rate

print("Total hours:",total_hours)
print("Total pay:",total_pay)