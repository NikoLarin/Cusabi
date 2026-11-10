import random

def division_problem(min, max):  # min/max parameters create the range
    dividend = random.randint(min, max)
    target = dividend * random.randint(min, max)
    divisor = int(target / dividend)

    return (dividend, divisor, target)

dividend, divisor, target = division_problem(1,100)

