import prompt
from brain_games.cli import welcome_user


def game(name_game, rules):
    rules = rules()
    name = welcome_user()
    counter = 0

    print(rules)
    while counter < 3:
        question, ans = name_game()
        print("Question:", question)
        us_ans = prompt.string("Your answer:")
        if str(ans) == us_ans:
            counter += 1
            print("Correct!")
        else:
<<<<<<< HEAD
            print(f" '{us_ans}' is wrong answer ;(. Correct answer was '{ans}'.")
=======
            print(f" '{us_ans}' is wrong answer ;(. Correct answer was '{ans}'")
>>>>>>> parent of 43f9768 (Delete brain_games/engine.py)
            print(f"Let's try again, {name}! ")
            return counter
    if counter == 3:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    game()
