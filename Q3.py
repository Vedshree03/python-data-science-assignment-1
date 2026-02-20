# List of numbers
nums = [12, 45, 7, 89, 23, 56, 34, 90, 11, 67]

# Assume first number is maximum
max_num = nums[0]

# Compare each number
for n in nums:
    if n > max_num:
        max_num = n

print("Maximum number is:", max_num)