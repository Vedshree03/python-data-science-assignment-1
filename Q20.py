# Set to store prime numbers
primes = set()

# Check prime numbers from 1 to 100
for num in range(2, 101):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        primes.add(num)

# Dictionary to group primes by digit sum
result = {}

for p in primes:
    digit_sum = sum(int(d) for d in str(p))
    result.setdefault(digit_sum, []).append(p)

print(result)