# Name: Sonali Banne

emp = {
    "name": "Rohan",
    "dept": "Analytics",
    "salary": 45500
}

emp["city"] = "Pune"
emp["salary"] = emp["salary"] + 5000
emp.pop("dept")

for key, value in emp.items():
    print(f"{key}: {value}")