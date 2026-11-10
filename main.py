import random
from addition_problem import *
from division_problem import *
from multiplication_problem import *
from subtraction_problem import *

if __name__ == "__main__":
    problem_range_min = 1
    problem_range_max = 100
    problem_choice = random.randint(4,4)

    if problem_choice == 1: #addition
        addend1, addend2, answer = addition_problem(problem_range_min, problem_range_max)
        user_answer = input(f"{addend1} + {addend2} = ")

    if problem_choice == 2: #subtraction
        minuend, subtrahend, answer = subtraction_problem(problem_range_min, problem_range_max)
        user_answer = input(f"{minuend} - {subtrahend} = ")

    if problem_choice == 3: # multiplication
        multiplicand, multiplier, answer = multiplication_problem(problem_range_min, problem_range_max)
        user_answer = input(f"{multiplicand} * {multiplier} = ")
        
    if problem_choice == 4: #division
        divisor, answer, target = division_problem(problem_range_min, problem_range_max)
        user_answer = input(f'{target} / {divisor} = ')

    if answer == int(user_answer):
        print("Correct")
    else:
        print("Wrong")
        print(answer)