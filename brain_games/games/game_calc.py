import prompt
import random
from brain_games.scripts.cli import main
from brain_games.drive import ans_validator


def run(NUM_CORRECT_ANS=0):
    name = main()
    print("What is the result of the expression?")
    while NUM_CORRECT_ANS < 3:
        generated_random_num_1: int = random.randint(1, 100)
        generated_random_num_2 = random.randint(1, 100)
        rand_operation = random.randint(0, 2)
        lst_operations = ["+", "-", "*"]
        print(f'Question: {generated_random_num_1}', end="")
        print(f' {lst_operations[rand_operation]} {generated_random_num_2}')
        right_ans = eval(f"{generated_random_num_1}\
             {lst_operations[rand_operation]} {generated_random_num_2}")
        ans = prompt.string('Your answer:')
        NUM_CORRECT_ANS = ans_validator(ans, right_ans, name, NUM_CORRECT_ANS)
        if NUM_CORRECT_ANS == 0:
            break
