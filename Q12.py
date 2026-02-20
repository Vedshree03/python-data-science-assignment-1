# Dictionary with student grades
students = {
    "A": [80, 90, 85],
    "B": [70, 60, 75],
    "C": [95, 92, 90],
    "D": [88, 84, 86]
}

averages = {}

# Calculate average marks
for student, grades in students.items():
    averages[student] = sum(grades) / len(grades)

# Sort and get top 3 students
top_students = sorted(averages.items(), key=lambda x: x[1], reverse=True)[:3]

print("Top 3 students:", top_students)