import random
import prompt
from brain_games.cli import welcome_user

def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 1
    while count <= 3:
        random_number = random.randint(1, 100)
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        correct_answer = "yes" if random_number % 2 == 0 else "no"

        if answer == correct_answer:
            print("Correct!")
            count += 1
        else:
            count = 1
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
    print(f"Congratulations, {name}!")

if __name__ == "__main__":
    main()

