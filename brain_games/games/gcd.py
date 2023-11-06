import random
import math
from brain_games.const import GCD_INSTRUCTION
from brain_games.drive import user_response_request


def return_r_ans_gcd():
    generated_random_num_1: int = random.randint(1, 100)
    generated_random_num_2 = random.randint(1, 100)
    question = f'Question: {generated_random_num_1} {generated_random_num_2} '
    r_ans = math.gcd(generated_random_num_1, generated_random_num_2)
    return [r_ans, question]


def start_game_gcd():
    user_response_request(GCD_INSTRUCTION, return_r_ans_gcd)
