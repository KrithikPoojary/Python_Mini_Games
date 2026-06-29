import random

#function of game is to be played between user and bot
def game():
    bot = random.choice([1 , 2  ,3])   #here bot choose his random choice
    a = input("Enter your choice: ")
    dict1 = {"rock" : 1 , "paper" : 2 , "scissor" : 3}  
    dict2 = { 1 : "Rock" , 2 : "Paper" , 3 : "scissor"}
    you = dict1[a]
    print(f"bot choose {dict2[bot]}\nyou choose {a} ")  #This line will print the choice of bot and user

#After the choice of bot and user we will check who wins the game

    if bot == you:
        print("Game tie!")
    elif bot==1 and you ==2:
        print("You wins!")
    elif bot==1 and you ==3:
        print("You lost :)")
    elif bot==2 and you ==1:
        print("You lost :)")
    elif bot==2 and you ==3:
        print("You wins!")
    elif bot == 3 and you == 1:
        print("You wins!")
    elif bot==3 and you ==2:
        print("You lost :)")
    else:
        print("Something went wrong!!!!!")

#Then we will call the function to play the game 

game()