import random

RULES = 'What is the result of the expression?'


def answer(random_num1, random_num2, random_op):
    answer = " "
    if random_op == "+":
        answer = random_num1 + random_num2
    elif random_op == "-":
        answer = random_num1 - random_num2
    else:
        answer = random_num1 * random_num2
    return answer


def generate_round():
    random_num1 = random.randint(1, 100)
    random_num2 = random.randint(1, 100)
    random_op = random.choice(["+", "-", "*"])
    question = str(random_num1) + " " + (random_op) + " " + str(random_num2)
    right_answer = answer(random_num1, random_num2, random_op)
    return question, right_answer
