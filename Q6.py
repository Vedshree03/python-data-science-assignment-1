# Empty list to store table
table = []

# Nested loops for multiplication
for i in range(1, 11):
    for j in range(1, 11):
        table.append((i, j, i * j))   # storing as tuple

print(table)