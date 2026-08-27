import random


def roll():
    min_value = 1
    max_value = 6
    dice = random.randint(min_value, max_value)

    return dice


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
players_scores = [0 for _ in range(players)]


while max(players_scores) < max_score:

    for player_idx in range(players):

        print(f"\nPlayer {player_idx + 1} Turn has just started")

        current_score = 0

        while True:

            a = input("Do you want to roll [y/n]? ").lower()

            if a != "y":
                break

            b = roll()

            if b == 1:
                print("You rolled a: 1! Turn done")
                current_score = 0
                break

            else:
                current_score += b
                print(f"You rolled a: {b}!")

            print(f"Your score = {current_score}")

        players_scores[player_idx] += current_score

        print(f"Your Total score is: {players_scores[player_idx]}")

        # Check if player reached 50
        if players_scores[player_idx] >= max_score:
            print(f"\nPlayer {player_idx + 1} reached {max_score}!")
            break


# Find winner
winner = players_scores.index(max(players_scores))

print("\n====================")
print("     GAME OVER!")
print("====================")

print(
    f"Player {winner + 1} wins "
    f"with {players_scores[winner]} points!"
)

print("\nFinal Scores:")

for player_idx in range(players):
    print(
        f"Player {player_idx + 1}: "
        f"{players_scores[player_idx]}"
    )