import random

n = random.randint(1 , 100)   #Bot will choose a random number between 1 to 100

a = -1  #Here we have taken -1 for 'a' because we want to run the loop until the user guess the correct number

guesses= 1  #This will keep track of the number of guesses the user has made

#here we will run a loop until the user guess the correct number
while(a != n):
    a = int(input("Guess the correct number: "))
    if (a < n):
        print("Highier number please!!")
        guesses += 1
    elif(a>n):
        print('lower number please!!')
        guesses += 1
    else:
        print(f"You have guessed the number {n} in {guesses} attempt")


        #Once the user guess the correct number we will print the number of attempts the user has made to guess the correct number