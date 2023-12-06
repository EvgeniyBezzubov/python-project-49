from brain_games.const import CALC_INSTRUCTION, \
    LST_OPERATIONS
from brain_games.engine import start_game
from brain_games.utils import rand
from random import choice


def get_result_by_math_operation(
        num_1,
        operation,
        num_2):
    if operation == "+":
        ans = num_1 + num_2
        return ans
    elif operation == "-":
        ans = num_1 - num_2
        return ans
    elif operation == "*":
        ans = num_1 * num_2
        return ans


def get_math_expression_result():
    num_1, num_2 = rand(), rand()
    rand_operation = choice(LST_OPERATIONS)
    question = f'{num_1} ' \
               f'{rand_operation} {num_2}'
    right_ans = get_result_by_math_operation(
        num_1, rand_operation, num_2)
    return question, str(right_ans)


def start_game_calc():
    start_game(CALC_INSTRUCTION, get_math_expression_result)
