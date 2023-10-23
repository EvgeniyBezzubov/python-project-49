import prompt
import random
from brain_games.scripts.cli import main
from brain_games.drive import ans_validator


def run(COUNT_TRUE_ANS=0):
    name = main()
    while COUNT_TRUE_ANS < 3:
        generated_random_num = random.randint(1, 100)
        print('Answer "yes" if the number is even, otherwise answer "no".')
        print('Question:', generated_random_num)
        user_answer = prompt.string('Your answer:')
        if generated_random_num % 2 == 1:
            correct_answer = "no"
        else:
            correct_answer = "yes"

        COUNT_TRUE_ANS = ans_validator(user_answer, correct_answer,
                                       name, COUNT_TRUE_ANS)
        if COUNT_TRUE_ANS == 0:
            break
