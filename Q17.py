# Nested dictionary
school = {
    "ClassA": {"S1": [80, 90], "S2": [70, 75]},
    "ClassB": {"S3": [60, 65]}
}

# Function to calculate average
def calculate_average(data):
    total = 0
    count = 0

    for class_data in data.values():
        for grades in class_data.values():
            total += sum(grades)
            count += len(grades)

    return total / count

print("Class average:", calculate_average(school))