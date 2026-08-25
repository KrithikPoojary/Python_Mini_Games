import random

def roll():
    min_value = 1
    max_value = 6
    dice = random.randint(min_value,max_value)

    return roll

while True:

    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        pass
    else:
        print("Invalid choice!! Try again.")