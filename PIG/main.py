import random

def roll():
    min_value = 1
    max_value = 6
    dice = random.randint(min_value,max_value)

    return roll

while True:

    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Player should be between 2 - 4")

    else:
        print("Invalid choice!! Try again.")

max_score = 50
players_scores = [0 for _  in range(players)]


while max(players_scores) > max_score:
    a = input('Do you want to roll [y/n]? ').lower()
    if a != "y":
        break
    b = roll()
    if b == 1:
        print("You rolled a 1! turn done")
        
    