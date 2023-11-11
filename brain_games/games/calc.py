from brain_games.const import calc_instruction
import random
from brain_games.drive import start_game


def return_r_ans_calc():
    generated_random_num_1: int = random.randint(1, 100)
    generated_random_num_2 = random.randint(1, 100)
    rand_operation = random.randint(0, 2)
    lst_operations = ["+", "-", "*"]
    question = f'Question: {generated_random_num_1} \
{lst_operations[rand_operation]} {generated_random_num_2}'
    right_ans = eval(f"{generated_random_num_1}\
         {lst_operations[rand_operation]} {generated_random_num_2}")
    return [right_ans, question]


def start_game_calc():
    start_game(calc_instruction, return_r_ans_calc)
