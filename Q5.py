# Function to return unique elements from list
def get_unique_list(lst):
    # Set removes duplicate values
    unique_set = set(lst)
    return list(unique_set)

print(get_unique_list([1, 2, 2, 3, 4, 4, 5]))