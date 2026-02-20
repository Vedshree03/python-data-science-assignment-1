import random

# Generate random numbers
numbers = [random.randint(1, 100) for _ in range(20)]

frequency = {}

# Count frequency
for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

# Find most common number
most_common = max(frequency, key=frequency.get)

print("Most common number:", most_common)