import time

class play:

    def __init__(self):
        print("")
        print("Three ancient swords rest upon a stone altar.\n"
            "Only one carries the power to defeat the guardian of the temple.\n"
            "The other two are cursed.\n"
            "Choose wisely... your decision will be revealed only at the end of your journey.\n\n"
            "\"Read the ancient inscription before you choose..\"\n"
            "##-- When the light fades and shadows rise, the blade that walks with darkness shall reveal the path of the chosen. --##\n"
            "Sword1 - Eclipse Fang\n"
            "Sword2 - Dragonbane\n"
            "Sword3 - Soulreaver")

        self.w = int(input("Choose your option: "))

    def play_logic(self):

        player_health = 100
        guardian_health = 100

        print("\nThe ancient Dragon awakens!")
        print("Guardian: \"You dare challenge me, mortal?\"")

        if self.w == 1:
            sword = "Eclipse Fang"
        elif self.w == 2:
            sword = "Dragonbane"
        elif self.w == 3:
            sword = "Soulreaver"
        else:
            print("Invalid sword choice!")
            return

        print(f"You raise the {sword}. Its blade begins to glow with dark energy.\n")

        print("Dragon wakes up!!")
        print("1 - Fight")
        print("2 - Run Away")
        print("3 - Hide")

        g = int(input("Choose your option: "))

        if g == 2 or g == 3:
            print("GAME OVER")
            return

        if g != 1:
            print("Invalid choice!")
            return

        while player_health > 0 and guardian_health > 0:

            print("Your Health:", player_health)
            print("Guardian Health:", guardian_health)

            print("\nChoose your action:")
            print("1. Slash Attack")
            print("2. Shadow Strike")
            print("3. Defend")

            choice = input("Enter your choice: ")

            if choice == "1":
                guardian_health -= 20
                print("\nYou strike the guardian with the {sword}")
                print("Guardian loses 20 health.")

            elif choice == "2":
                guardian_health -= 35
                print("\n🌑 You unleash the Shadow Strike!")
                print("Dark shadows surround the guardian.")
                print("Guardian loses 35 health.")

            elif choice == "3":
                print("\n🛡️ You defend yourself!")
                player_health -= 5
                print("Guardian attacks, but you block most of the damage.")
                continue

            else:
                print("\nInvalid choice! The guardian attacks you.")

            if guardian_health > 0:
                player_health -= 15
                print("\n⚔️ The guardian attacks you!")
                print("You lose 15 health.")

            print("\n" + "-" * 40 + "\n")

        if guardian_health <= 0:
            print("🏆 YOU DEFEATED THE GUARDIAN!")
            print(f"The {sword} has proven itself worthy.")
            print("The ancient temple recognizes you as the chosen one.")

        elif player_health <= 0:
            print("💀 YOU HAVE BEEN DEFEATED!")
            print("The guardian protects the temple once again.")
            print("GAME OVER")