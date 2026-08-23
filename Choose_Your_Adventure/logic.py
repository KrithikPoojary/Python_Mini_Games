import time
class play():
        print("")
        print("Three ancient swords rest upon a stone altar.\nOnly one carries the power to defeat the guardian of the temple.\nThe other two are cursed.\nChoose wisely... your decision will be revealed only at the end of your journey.\n\n\"Read the ancient inscription before you choose..\"\n##-- When the light fades and shadows rise, the blade that walks with darkness shall reveal the path of the chosen. --##\nSword1 - Eclipse Fang\nSword2 - Dragonbane\nSword3 - Soulreaver")
        w = int(input("Choose your option: ")).lower()
        time.sleep(1)
        print("")
        print("Dragon wakes up!!\n1 - Fight\n2 - Run Away\n3 - Hide")
        g = int(input("Choose your option: "))
        if g == 1:
            from logic import play
            a = play()
            b = a.play_logic()
            print(b)
        elif g == 2:
            print("GAME OVER")
            exit
        elif g == 3:
            print("GAME OVER")
            exit
        def play_logic(self):
            player_health = 100
            guardian_health = 100

            print("\nThe ancient Dragon awakens!")
            print(f"Guardian: \"You dare challenge me, nigga?\"")
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
                exit


a = play()
b = a.play_logic()
print(b)