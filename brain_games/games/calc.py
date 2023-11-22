from brain_games.const import CALC_INSTRUCTION, \
    LST_OPERATIONS
import random
from brain_games.engine import start_game
from brain_games.utils import rand_int_1_100


def return_right_ans_and_question():
    generated_random_num_1 = rand_int_1_100
    generated_random_num_2 = rand_int_1_100
    rand_num_for_operation = random.choice([x for x in range(3)])
    rand_operation = LST_OPERATIONS[rand_num_for_operation]
    question = f'Question: {generated_random_num_1} ' \
               f'{rand_operation} {generated_random_num_2}'
    right_ans = str(get_nums_and_return_right_ans(
        generated_random_num_1, rand_operation, generated_random_num_2))
    return right_ans, question


def start_game_calc():
    start_game(CALC_INSTRUCTION, return_right_ans_and_question)


def get_nums_and_return_right_ans(
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
