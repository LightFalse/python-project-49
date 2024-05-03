from random import randint


def progression():
    progression_lenght = randint(5, 10)
    start = randint(1, 10)
    step = randint(3, 15)
    random = randint(1, progression_lenght)
    progression = " "
    right_answer = start + (random - 1) * step
    for i in range(progression_lenght):
        result = start + i * step
        progression = progression + f'{str(result)}' + " "
    question = progression.replace(f' {str(right_answer)} ', " .. ")
    question = question.strip()
    return question, right_answer


def rules():
    rules = 'What number is missing in the progression?'
    return rules
