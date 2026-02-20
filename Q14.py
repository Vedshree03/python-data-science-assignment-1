# Shopping cart with items and prices
cart = [
    {"item": "Pen", "price": 40},
    {"item": "Book", "price": 70}
]

# Calculate total price
total = 0
for product in cart:
    total += product["price"]

# Apply discount if total > 100
if total > 100:
    total = total * 0.9

print("Final amount:", total)