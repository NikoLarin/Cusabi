import random

def multiplication_problem(min, max):
    multiplicand = random.randint(min, max)
    multiplier = random.randint(min, max)
    answer = multiplicand * multiplier

    return multiplicand, multiplier, answer
