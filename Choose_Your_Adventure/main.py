import time
print("**********************************************")
print("Welcome to Your_Adventure Game")
print("**********************************************")
print('''
==========================================================
            🏛️  THE LOST TEMPLE ADVENTURE  🏛️
==========================================================

Welcome, Adventurer!

Legends speak of an ancient temple hidden deep within
an uncharted forest. Inside lies a treasure that has
never been claimed... because no one has ever returned.

Your mission is simple:
Enter the temple.
Make the right decisions.
Survive every challenge.
Escape with the legendary treasure.

-Be careful!
Every choice you make matters.
One wrong decision can end your journey instantly.

There are no second chances...
Think before you choose.

Good luck, Adventurer.
Your fate begins now...


==========================================================
            Press Any key to start your adventure...
==========================================================
''')
user = input("").upper()

print("[You wake up at the entrance of the Lost Temple.\nLets Start...]")
time.sleep(1)
print("")
print("Which path do you take?\n1 - Left Forest\n2 - Right Swamp\n3 - Climb Mountain")
a = int(input("Choose your option: "))
if a == 1:
    print("")
    print('You find a river.\n1 - Build a Raft\n2 - Swim\n3 - Go Back')
    b = int(input("Choose your option: "))
    if b ==1 :
        print("")
        print("You reach a cave.\n1 - Enter Cave\n2 - Walk Around\n3 - Return")
        c = int(input("Choose your option: "))
        if c == 1:
            print("You Entered Cave\n1 - Left Tunnel\n2 - Middle Tunnel\n3 - Right Tunnel")
            d = int(input("Choose your option: "))
            if d == 1:
                print("There is Spike trap!!\nGAME OVER")
            if d == 2:
                print("")
                print("A locked door.\n1 - Solve Puzzle\n2 - Break Door\n3 - Search Another Way")
                e = int(input("Choose your option: "))
                if e == 1:
                    print("")
                    print('''"I speak without a mouth, I hear without ears, I have no body, but I come alive with the wind. What am I? \n1. Shadow \n2. Echo \n3. Fire \n4. Water): "''')
                    z = int(input("Enter your choice: "))
                    if z == 1:
                        print("Oh you are wrong....\nGAME OVER")
                    if z == 2:
                        print("")
                        print("You are Teleported to one Treasure room.\n1 - Take Treasure Immediately\n2 - Observe Room First\n3 - Leave")
                        f = int(input("Choose your option: "))
                        if f == 1 :
                            print("Seems like Dragon wakes!!!!\nGAME OVER")
                        elif f == 2:
                            print("")
                            print("Three ancient swords rest upon a stone altar.\nOnly one carries the power to defeat the guardian of the temple.\nThe other two are cursed.\nChoose wisely... your decision will be revealed only at the end of your journey.\n\n\"Read the ancient inscription before you choose..\"\n##-- When the light fades and shadows rise, the blade that walks with darkness shall reveal the path of the chosen. --##\nSword1 - Eclipse Fang\nSword2 - Dragonbane\nSword3 - Soulreaver")
                            
                        elif f == 3 :
                            print("GAME OVER")
                    if z == 3:
                        print("Oh you are wrong....\nGAME OVER")
                    if z == 4:
                        print("Oh you are wrong....\nGAME OVER")
                if e == 2:
                    print("Alarm!!!!!\nGAME OVER")
                if e == 3:
                    print("GAME OVER")
            if d == 3:
                print("There is Giant spider!!\n GAME OVER")
        if c ==2 :
            print('Quicksand!!!\nGAME OVER')
            exit
        if c == 3:
            print("GAME OVER")
    elif b ==2 :
        print("There is Crocodiles...\nGAME OVER")
        exit
    elif b == 3:
        print('Bandits attack..\nGAME OVER')
        exit
    else:
        print('Something went wrong!!')
elif a == 2:
    print("There is Poisonous snakes...\nGAME OVER)")
    exit
elif a == 3:
    print("Ohh You Fall from cliff.....\nGAME OVER")
    exit
else:
    print('Something went wrong!')
