# snake gun and water game 

import random

bot = random.choice([1 , 0 , -1])  #bot choose his random choice
you = input("Enter your choice: ")
dict1= {"snake" : 1 , "water" : 0 , "gun" : -1 }
dict2={1 : "Snake" , 0 : "Water" , -1 : "Gun"}
a = dict1[you]

print(f"bot choose: {dict2[bot]}\nyou choose: {dict2[a]}") #Here we will print the choice of bot and user

#And then we will check who wins the game

if(bot == a):
    print("it is draw!!!")

else: 
    if(bot == 1 and a == 0):
        print("bot wins")
    elif(bot == 1 and a == -1):
        print("you wins!!!")
    elif(bot==0 and a==1):
        print("you wins!!!")
    elif(bot==0 and a == -1):
        print("bot wins")
    elif(bot==-1 and a==1):
        print("bot wins")
    elif(bot==-1 and a == 0):
        print("you winss!!!")
    else:
        print("something went wrong!")