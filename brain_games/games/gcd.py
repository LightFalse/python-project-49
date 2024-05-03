import random
import math


def gcd():
    random_num1 = random.randint(1, 100)
    random_num2 = random.randint(1, 100)
    question = (f"{random_num1} {random_num2}")
    right_answer = math.gcd(random_num1, random_num2)
    return question, right_answer


def rules():
    rules = 'Find the greatest common divisor of given numbers.'
    return rules
