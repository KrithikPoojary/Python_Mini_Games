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
    