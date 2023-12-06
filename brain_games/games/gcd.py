import math
from brain_games.const import GCD_INSTRUCTION
from brain_games.engine import start_game
from brain_games.utils import rand


def get_math_expression_result():
    generated_random_num_1 = rand
    generated_random_num_2 = rand
    question = f'{generated_random_num_1} {generated_random_num_2}'
    r_ans = math.gcd(generated_random_num_1, generated_random_num_2)
    return question, str(r_ans)


def start_game_gcd():
    start_game(GCD_INSTRUCTION, get_math_expression_result)
