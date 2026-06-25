import prompt
from brain_games.cli import welcome_user

def run_games(game):
    name = welcome_user()
    print(game.DESCRIPTION)
    count = 0
    while count < 3:
        question, correct_answer = game.creating_game_logic()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

       

        if answer == str(correct_answer):
            print("Correct!")
            count += 1
        else:
            
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
            
    print(f"Congratulations, {name}!")