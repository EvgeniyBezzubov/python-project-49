from brain_games.const import CALC_INSTRUCTION
import random
from brain_games.drive import user_response_request


def return_r_ans_calc():
    generated_random_num_1: int = random.randint(1, 100)
    generated_random_num_2 = random.randint(1, 100)
    rand_operation = random.randint(0, 2)
    lst_operations = ["+", "-", "*"]
    question = f'Question: {generated_random_num_1} {lst_operations[rand_operation]} {generated_random_num_2}'
    right_ans = eval(f"{generated_random_num_1}\
         {lst_operations[rand_operation]} {generated_random_num_2}")
    return [right_ans, question]


def start_game_calc():
    user_response_request(CALC_INSTRUCTION, return_r_ans_calc)
