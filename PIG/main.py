import random

def roll():
    min_value = 1
    max_value = 6
    dice = random.randint(min_value,max_value)

    return roll


players = int(input("Enter the number of players (2 - 4): "))