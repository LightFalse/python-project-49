import prompt
from brain_games.cli import welcome_user


def game(question, right_answer):
    name = welcome_user()
    counter = 0
    while counter < 3:
        print(question) 
        player_answer= prompt.string("Your answer:")
        if right_answer == int(player_answer): 
            counter += 1
            print("Correct!")
        else:
            print(f" {player_answer} is wrong answer ;(. Correct answer was {right_answer}. /nLet's try again, {name}! ")
            return counter
    if counter == 3:   
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    game()  