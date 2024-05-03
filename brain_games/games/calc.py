import random





def calc():
    random_num1 = random.randint(1, 100)
    random_num2 = random.randint (1, 100)
    random_operation=random.choice(["+","-","*"])
    question = (str(random_num1)+ random_operation+str(random_num2))
    right_answer = eval(f"{random_num1} {random_operation} {random_num2}")
    return question, right_answer


def rules():
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    return rules


if __name__ == "__main__":
    calc()

    
    
    
    

#def question:
#    
#    return question