import random


def prime():
    question = random.randint(2, 101)
    i = 2
    right_answer = "no"
    while question % i != 0:
        i += 1
        if i == question:
            right_answer = "yes"
        else:
            continue
    return question, right_answer


def rules():
    rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    return rules
