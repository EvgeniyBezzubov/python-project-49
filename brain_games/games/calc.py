from brain_games.const import CALC_INSTRUCTION, \
    LST_OPERATIONS
from brain_games.engine import start_game
from brain_games.utils import get_random_num
from random import choice


def get_result_by_math_operation(
        num_1,
        operation,
        num_2):
    if operation == "+":
        return num_1 + num_2
    elif operation == "-":
        return num_1 - num_2
    elif operation == "*":
        return num_1 * num_2


def get_math_expression_and_result():
    num_1, num_2 = get_random_num(), get_random_num()
    rand_operation = choice(LST_OPERATIONS)
    math_expression = f'{num_1} ' \
                      f'{rand_operation} {num_2}'
    result = get_result_by_math_operation(num_1, rand_operation, num_2)
    return math_expression, str(result)


def start_game_calc():
    start_game(CALC_INSTRUCTION, get_math_expression_and_result)
