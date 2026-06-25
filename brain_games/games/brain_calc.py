import random

DESCRIPTION = ('What is the result of the expression?')

def creating_game_logic():
    random_number1 = random.randint(1, 100)
    random_number2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])
    qestion = f"{random_number1}{operator}{random_number2}"

    match operator:
            case '+':
                correct_answer = random_number1 + random_number2
            case '-':
                correct_answer = random_number1 - random_number2
            case '*':
                correct_answer = random_number1 * random_number2
        
    return qestion, correct_answer
