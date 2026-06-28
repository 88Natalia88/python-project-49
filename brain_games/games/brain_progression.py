import random

DESCRIPTION = ('What number is missing in the progression?')

def creating_game_logic():
    random_number = random.randint(1, 100)
    random_step = random.randint(1, 10)
    random_lenght = random.randint(5, 10)
    random_array = []

    for i in range(random_lenght):
        currentElement = random_number + i * random_step
        random_array.append(currentElement)
    
    random_hidden_number = random.choice(random_array)
    hidden_index = random_array.index(random_hidden_number)

    random_array[hidden_index] = '..'
    question = " ".join(str(x) for x in random_array)


    correct_answer = str(random_hidden_number)

        
    return question, correct_answer
