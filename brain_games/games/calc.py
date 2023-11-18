from brain_games.const import CALC_INSTRUCTION, \
    START_NUM_FOR_RANDOMIZE_1, LST_OPERATIONS, END_NUM_FOR_RANDOMIZE_100
import random
from brain_games.engine import start_game
from brain_games.utils import rand_int


def return_right_ans_and_question():
    generated_random_num_1: int = rand_int(START_NUM_FOR_RANDOMIZE_1,
                                           END_NUM_FOR_RANDOMIZE_100)
    generated_random_num_2 = rand_int(START_NUM_FOR_RANDOMIZE_1,
                                      END_NUM_FOR_RANDOMIZE_100)
    rand_num_for_operation = random.randint(0, 2)
    rand_operation = LST_OPERATIONS[rand_num_for_operation]
    question = f'Question: {generated_random_num_1} ' \
               f'{rand_operation} {generated_random_num_2}'
    right_ans = str(use_opertaion_on_numbers_and_return_right_ans(
        generated_random_num_1, rand_operation, generated_random_num_2))
    return right_ans, question


def start_game_calc():
    start_game(CALC_INSTRUCTION, return_right_ans_and_question)


def use_opertaion_on_numbers_and_return_right_ans(
        generated_random_num_1,
        rand_operation,
        generated_random_num_2):
    if rand_operation == "+":
        ans = generated_random_num_1 + generated_random_num_2
    elif rand_operation == "-":
        ans = generated_random_num_1 - generated_random_num_2
    elif rand_operation == "*":
        ans = generated_random_num_1 * generated_random_num_2
    return ans