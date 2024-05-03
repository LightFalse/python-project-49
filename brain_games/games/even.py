import random


def even():
    random_num = random.randint(1, 100)
    question = random_num
    if random_num % 2 == 0:
        right_answer = str("yes")
    else:
        right_answer = str("no")
    return question, right_answer


def rules():
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    return rules
