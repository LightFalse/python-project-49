import prompt
from brain_games.cli import welcome_user


def game(generate_options):
    rules = generate_options.RULES
    name = welcome_user()
    counter = 0
    MAX_ROUND = 3

    print(rules)
    while counter < MAX_ROUND:
        question, ans = generate_options.generate_round()
        print("Question:", question)
        us_ans = prompt.string("Your answer:")
        if str(ans) == us_ans:
            counter += 1
            print("Correct!")
        else:
            print(f"'{us_ans}' is wrong answer ;(. Correct answer was '{ans}'")
            print(f"Let's try again, {name}! ")
            return counter
    if counter == 3:
        print(f"Congratulations, {name}!")
