# Function to print even numbers from 1 to 20
def print_even_numbers():
    i = 1                  # starting number
    while i <= 20:         # loop until 20
        if i % 2 == 0:     # check if number is even
            print(i)
        i += 1             # move to next number

print_even_numbers()