import random
from brain_games.const import CALC_INSTRUCTION, OPERATIONS
from brain_games.engine import start_game
from brain_games.utils import get_random_num



def get_result_by_math_operation(num1, operation, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2


def get_math_expression_and_result():
    num1, num2 = get_random_num(), get_random_num()  # пролистал несколько страниц гугла,
    rand_operation = random.choice(OPERATIONS)  # что такое клвалификационное имя не понял, написал, как подумал.
    math_expression = f'{num1} ' \
                      f'{rand_operation} {num2}'
    result = get_result_by_math_operation(num1, rand_operation, num2)
    return math_expression, str(result)


def start_game_calc():
    start_game(CALC_INSTRUCTION, get_math_expression_and_result)
