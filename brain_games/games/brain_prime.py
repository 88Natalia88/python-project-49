import random

DESCRIPTION = ('Answer "yes" if given number is prime. Otherwise answer "no".')

def creating_game_logic():
    random_number = random.randint(1, 100)
    question = random_number

    if random_number == 1:
       correct_answer = 'no'
    else:
        correct_answer = 'yes'
        for i in range(2, int(random_number**0.5) + 1):
            if random_number % i == 0:
                correct_answer = 'no'
                break
 
    return question, correct_answer
