class play():
        def play_logic(self):
            player_health = 100
            guardian_health = 100

            print("\nThe ancient Dragon awakens!")
            print(f"Guardian: \"You dare challenge me, {a12}?\"")
            print("You raise the Eclipse Fang. Its blade begins to glow with dark energy.\n")

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
                    print("\nYou strike the guardian with the Eclipse Fang!")
                    print("Guardian loses 20 health.")

                elif choice == "2":
                    guardian_health -= 35
                    print("\n🌑 You unleash the Shadow Strike!")
                    print("Dark shadows surround the guardian.")
                    print("Guardian loses 35 health.")

                elif choice == "3":
                    print("\n🛡️ You defend yourself!")
                    print("The guardian's attack will deal less damage.")

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
                print("The Eclipse Fang has proven itself worthy.")
                print("The ancient temple recognizes you as the chosen one.")

            elif player_health <= 0:
                print("💀 YOU HAVE BEEN DEFEATED!")
                print("The guardian protects the temple once again.")
                print("GAME OVER")


a = play()
b = a.play_logic()
print(b)