import math
from brain_games.const import GCD_INSTRUCTION, \
    START_NUM_FOR_RANDOMIZE_1, END_NUM_FOR_RANDOMIZE_100
from brain_games.engine import start_game
from brain_games.utils import rand_int


def return_right_ans_and_question():
    generated_random_num_1: int = rand_int(START_NUM_FOR_RANDOMIZE_1,
                                           END_NUM_FOR_RANDOMIZE_100)
    generated_random_num_2 = rand_int(START_NUM_FOR_RANDOMIZE_1,
                                      END_NUM_FOR_RANDOMIZE_100)
    question = f'Question: {generated_random_num_1} {generated_random_num_2}'
    r_ans = str(math.gcd(generated_random_num_1, generated_random_num_2))
    return r_ans, question


def start_game_gcd():
    start_game(GCD_INSTRUCTION, return_right_ans_and_question)
