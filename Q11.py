# List of (id, score)
data = [(1, 80), (2, 95), (3, 70)]

# Sort by score in descending order
sorted_data = sorted(data, key=lambda x: x[1], reverse=True)

# Print sorted result
for item in sorted_data:
    print(item)