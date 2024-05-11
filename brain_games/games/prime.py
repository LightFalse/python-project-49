import random

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime(number):
    divider = 2
    answer = "no"
    while number % divider != 0:
        divider += 1
        if divider == number:
            answer = "yes"
        else:
            continue
    return answer


def generate_round():
    question = random.randint(2, 101)
    right_answer = prime(question)
    return question, right_answer
