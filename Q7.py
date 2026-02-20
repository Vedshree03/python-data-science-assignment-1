# Dictionary with name and age
people = {"Asha": 22, "Ravi": 17, "Neha": 19}

# Loop using items()
for name, age in people.items():
    if age >= 18:
        print(name, "is an adult")