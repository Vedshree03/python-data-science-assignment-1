# List of student scores
scores = [45, 78, 60, 30, 90]

i = 0
pass_count = 0
fail_count = 0

# Using while loop
while i < len(scores):
    if scores[i] >= 60:
        pass_count += 1
    else:
        fail_count += 1
    i += 1

print("Passed:", pass_count)
print("Failed:", fail_count)