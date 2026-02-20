import random

choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
wins = set()

# Play 5 rounds
for i in range(5):
    user = random.randint(1, 3)
    computer = random.randint(1, 3)

    if user != computer:
        wins.add(user)

print("Winning choices:", wins)