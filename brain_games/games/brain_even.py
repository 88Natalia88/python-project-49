import random

DESCRIPTION = ('Answer "yes" if the number is even, otherwise answer "no".')

def creating_game_logic():
    random_number = random.randint(1, 100)
    correct_answer = "yes" if random_number % 2 == 0 else "no"

    question = random_number

    return question, correct_answer


