import math
from brain_games.const import gcd_instruction
from brain_games.engine import start_game
from brain_games.utils import rand_int
from brain_games.const import start_num_for_randomize_1
from brain_games.const import end_num_for_randomize_100


def return_right_ans_and_question():
    generated_random_num_1: int = rand_int(start_num_for_randomize_1,
                                           end_num_for_randomize_100)
    generated_random_num_2 = rand_int(start_num_for_randomize_1,
                                      end_num_for_randomize_100)
    question = f'Question: {generated_random_num_1} {generated_random_num_2}'
    r_ans = str(math.gcd(generated_random_num_1, generated_random_num_2))
    return [r_ans, question]


def start_game_gcd():
    start_game(gcd_instruction, return_right_ans_and_question)
