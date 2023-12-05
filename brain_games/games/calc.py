from brain_games.const import CALC_INSTRUCTION, \
    LST_OPERATIONS
import random
from brain_games.engine import start_game
from brain_games.utils import rand_1_100


def generate_math_func_and_result_calc():
    generated_random_num_1, generated_random_num_2 = rand_1_100(), rand_1_100()
    rand_operation = LST_OPERATIONS[random.randint(0, 2)]
    question = f'Question: {generated_random_num_1} ' \
               f'{rand_operation} {generated_random_num_2}'
    right_ans = str(get_result_by_math_operation(
        generated_random_num_1, rand_operation, generated_random_num_2))
    return right_ans, question


def get_result_by_math_operation(
        num_1,
        operation,
        num_2):
    if operation == "+":
        ans = num_1 + num_2
    elif operation == "-":
        ans = num_1 - num_2
    elif operation == "*":
        ans = num_1 * num_2
    return ans


def start_game_calc():
    start_game(CALC_INSTRUCTION, generate_math_func_and_result_calc)
