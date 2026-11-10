import random
import math
# Just ev

# different prompts framing the question
    #pay X to play, $8 on a win with 1/3 chance, -$4 on a loss with 2/3 chance.
        # variations of this

# random promt
# file with tons of prompts, pass in values call to the file where the prompts are and random number gen selects which prompt. 

# function to generate 3 random values which fit the prompt 
def math_problem(first_term: float, second_term: float):
    decision = random.randint(1, 4)
    rounded_first_term = round(first_term)
    rounded_second_term = round(second_term)

    if decision == 1: # addition
        print(f"{first_term} + {second_term}")
        answer = first_term + second_term

    elif decision == 2: # subtraction
        print(f"{first_term} - {second_term}")
        answer = first_term - second_term
    
    elif decision == 3: # multiplication
       
        print(f"{rounded_first_term} * {rounded_second_term}")
        answer = rounded_first_term * rounded_second_term
    
    else: #division  
        print(f"{rounded_first_term} / {rounded_second_term}")
        answer = math.floor(rounded_first_term / rounded_second_term)
    
    return round(answer,2)

first_term = round(random.uniform(-120.0, 120.0), 2)
second_term = round(random.uniform(-120.0, 120.0), 2)

answer = math_problem(first_term, second_term)
user_answer = float(input("Whats the solution?: "))

if user_answer == answer:
    print("Correct")
else:
    print(f"The answer was: {answer}")
    print(type(answer))