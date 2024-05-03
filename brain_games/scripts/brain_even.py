from brain_games.engine import game
from brain_games.games.even import even
from brain_games.games.even import rules


def main():
    game(even, rules)

if __name__ == "__main__":
    main()


# def game():
#     name=welcome_user()
#     right_answer = 0
#     print('Answer "yes" if the number is even, otherwise answer "no".')
#     while right_answer < 3:
#         random_num=random.randint(1, 100)      
#         print(random_num)
#         answer = prompt.string('Your answer: ')
#         if random_num % 2 == 0 and answer == "yes":
#             print("Correct!")
#             right_answer += 1
#         elif random_num % 2 != 0 and answer == "no":
#             print("Correct!")
#             right_answer += 1
#         elif random_num % 2 != 0 and answer == "yes":
#             print(f"'no' is wrong answer ;(. Correct answer was 'yes'./n Let's try again, {name}")
#             right_answer = 0
#             return right_answer
#         else:
#             print(f"'yes' is wrong answer ;(. Correct answer was 'no'./n Let's try again, {name}")
#             right_answer = 0
#             return right_answer

#     if right_answer == 3:
#         print(f"Congratulations, {name}!")




