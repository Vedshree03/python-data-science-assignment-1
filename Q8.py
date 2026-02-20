# Function to reverse a list
def reverse_list(lst):
    return lst[::-1]     # slicing method

my_list = [1, 2, 3, 4]
print("Reversed list:", reverse_list(my_list))

# Tuple example (immutable)
my_tuple = (1, 2, 3)
print("Reversed tuple:", my_tuple[::-1])