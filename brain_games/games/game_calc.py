from brain_games.const import CALC_INSTRUCTION
import random


def game_calc_run():
    print(CALC_INSTRUCTION)
    generated_random_num_1: int = random.randint(1, 100)
    generated_random_num_2 = random.randint(1, 100)
    rand_operation = random.randint(0, 2)
    lst_operations = ["+", "-", "*"]
    print(f'Question: {generated_random_num_1}', end="")
    print(f' {lst_operations[rand_operation]} {generated_random_num_2}')
    right_ans = eval(f"{generated_random_num_1}\
         {lst_operations[rand_operation]} {generated_random_num_2}")
    return right_ans
