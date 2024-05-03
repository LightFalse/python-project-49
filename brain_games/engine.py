import prompt
from brain_games.cli import welcome_user


def game(name_game, rules):
    rules = rules()
    name = welcome_user()
    counter = 0

    print(rules)
    while counter < 3:
        question, right_answer = name_game()
        print("Question:", question)
        player_answer = prompt.string("Your answer:")
        if str(right_answer) == player_answer:
            counter += 1
            print("Correct!")
        else:
            print(f" '{player_answer}' is wrong answer ;(. Correct answer was '{right_answer}'. \n Let's try again, {name}! ")
            return counter
    if counter == 3:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    game()
