tasks = ["email", "report", "meeting"]

tasks.append("review")
tasks.insert(0, "standup")

popped_item = tasks.pop()
print("Popped:", popped_item)

tasks.remove("meeting")
tasks.extend(["deploy", "test"])

print(tasks, len(tasks))
print("Report count:", tasks.count("report"))
print("Deploy index:", tasks.index("deploy"))