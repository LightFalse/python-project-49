import random
import prompt


print('Welcome to the Brain Games!')
name = prompt.string('May I have your name? ')
print(f'Hello, {name}!')


def game():
  right_answer = 0
  print('Answer "yes" if the number is even, otherwise answer "no".')

  while right_answer < 3:
    random_num=random.randint(1, 100)
    print(random_num)
    answer = prompt.string('Your answer: ')
    if random_num % 2 == 0 and answer == "yes":
      print("Correct!")
      right_answer += 1
    elif random_num % 2 != 0 and answer == "no":
      print("Correct!")
      right_answer += 1
    elif random_num % 2 != 0 and answer == "yes":
      print(f"'no' is wrong answer ;(. Correct answer was 'yes'. Let's try again, {name}")
      right_answer = 0
      return right_answer
      
    else:
      print(f"'yes' is wrong answer ;(. Correct answer was 'no'. Let's try again, {name}")
      right_answer = 0
      return right_answer

  if right_answer == 3:
    print(f"Congratulations, {name}!")

if __name__ == __main__:
  game()