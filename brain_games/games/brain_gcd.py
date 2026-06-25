import random

DESCRIPTION = ('Find the greatest common divisor of given numbers.')

def creating_game_logic():
    random_number1 = random.randint(1, 100)
    random_number2 = random.randint(1, 100)
    question = f"{random_number1} {random_number2}"

    while random_number2 != 0:
        
        random_number1 ,random_number2 = random_number2, random_number1 % random_number2

    correct_answer = str(random_number1)

    

    return question, correct_answer