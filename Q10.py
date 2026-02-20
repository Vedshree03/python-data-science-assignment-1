# Two sets of numbers
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)

# Difference using loop
for value in set1 - set2:
    print("Only in set1:", value)