import random
import time

OPERATORS = ["+" , "-" , "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_QUESTIONS = 10

def question():
    left = random.randint(MIN_OPERAND , MAX_OPERAND)
    right = random.randint(MIN_OPERAND ,MAX_OPERAND)
    operators = random.choice(OPERATORS)

    expression = str(left) + "" + operators + ""  + str(right)
    ans = eval(expression)  #SO eval is basically, if the operation is logical it finds the answers.
    return expression , ans


wrong = 0
Time_start = time.time()


input("Press enter to start: ")
print("------------------------")
for i in range(TOTAL_QUESTIONS):
    expression , ans = question()
    while True:
        guess = input(f"Question {i+1}- {expression}: ")
        if guess == str(ans):
            break
        wrong += 1

Time_end = time.time()
print("------------------------")
print(f"You have completed your challenge in {round(Time_end - Time_start,2)}sec and with {wrong} time correction")