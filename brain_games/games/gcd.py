import random

RULES = 'Find the greatest common divisor of given numbers.'


def gcd(random_num1, random_num2):
    while random_num2 != 0:
        (random_num1, random_num2) = (random_num2, random_num1 % random_num2)
    return random_num1


def generate_round():
    random_num1 = random.randint(1, 100)
    random_num2 = random.randint(1, 100)
    question = (f"{random_num1} {random_num2}")
    right_answer = gcd(random_num1, random_num2)
    return question, right_answer
