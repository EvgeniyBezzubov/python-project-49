import random
import math
from brain_games.const import gcd_instruction
from brain_games.drive import start_some_game


def return_r_ans_gcd():
    generated_random_num_1: int = random.randint(1, 100)
    generated_random_num_2 = random.randint(1, 100)
    question = f'Question: {generated_random_num_1} {generated_random_num_2} '
    r_ans = math.gcd(generated_random_num_1, generated_random_num_2)
    return [r_ans, question]


def start_game_gcd():
    start_some_game(gcd_instruction, return_r_ans_gcd)
