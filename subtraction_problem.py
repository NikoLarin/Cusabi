import random

def subtraction_problem(min, max):
    subtrahend = random.randint(min, max)
    minuend = subtrahend - random.randint(min, subtrahend)
    answer = subtrahend - minuend

    return minuend, subtrahend, answer