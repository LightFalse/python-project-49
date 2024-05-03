from random import randint


def progression():
    progression_lenght = randint(5, 10)
    start = randint(1, 10)
    step = randint(3, 15)
    random = randint(1, progression_lenght)
    progression = " "
    right_answer = start + (random - 1) * step
    for i in range(progression_lenght):
        x = start + i * step
        progression = progression + f'{str(x)}' + " "
    question = progression.replace(f' {str(right_answer)} ', " .. ")
    return question, right_answer


def rules():
    rules = 'What number is missing in the progression?'
    return rules


if __name__ == "__main__":
    progression()
