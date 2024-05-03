import random
from brain_games.engine import game


def calc():
    random_num1 = random.randint(1, 100)
    random_num2 = random.randint (1, 100)
    random_operation=random.choice(["+","-","*"])
    question = (str(random_num1)+ random_operation+str(random_num2))
    right_answer = eval(f"{random_num1} {random_operation} {random_num2}")
    return question

game(question, right_answer)


if __name__ == "__main__":
    calc()

    
    
    
    

#def question:
#    
#    return question