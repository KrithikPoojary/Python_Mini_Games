#Two user can play this game 

import random
import time

user1 = input("Enter the name: ")
user2 = input("Enter the name: ")
print("lets toss the coin..")
a = ["Tails" , "Heads"]
Coin = random.choice(a)    #The choice will be stored on coin , that is simple the result .
c = ["user1" , "user2"]
ump = f"Coin is flipping.... \nSo {Coin} it is"

#we will run it on loop whether user want to flip the coin again or not 
while True:
    x = random.choice(c)
    if x == c[0]:
        print(f"{user1} will choose")
        time.sleep(1)
        i = input("Enter Your Choice: ").capitalize()
        if i == "Heads":
            print(f"{user2} = Tails")
        elif i == "Tails":
            print(f"{user2} = Heads")
        else:
            print("Choose either Tails or Heads!")
            break
        print(ump)
        time.sleep(2)
        if i == Coin:
            print(f"{user1} wins")
        elif i != Coin:
            print(f"{user2} wins")

    elif x == c[1]:
        print (f"{user2} will choose")
        j = input("Enter Your Choice: ").capitalize()
        print(f"{user2} choose {j}")
        if j == "Heads":
            print(f"{user1} = Tails")
        elif j == "Tails":
            print(f"{user1} = Heads")
        else:
            print("Choose either Tails or Heads!")
            break
        print(ump)
        time.sleep(2)
        if j == Coin:
            print(f"{user2} wins")
        elif j != Coin:
            print(f"{user1} wins")

#This if_else will decide whether user wnat to run the loop or exit tha loop

    menu = input("Do want to play again? [y/n]").lower()
    if menu == "y":
        pass
    elif menu == "n":
        break
    else:
        print("Choose either y/n")
        break
    print("")



