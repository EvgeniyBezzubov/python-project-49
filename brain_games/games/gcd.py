import math
from brain_games.const import GCD_INSTRUCTION
from brain_games.engine import start_game
from brain_games.utils import rand


def get_math_expression_result():
    num_1 = rand()
    num_2 = rand()
    question = f'{num_1} {num_2}'
    r_ans = math.gcd(num_1, num_2)
    return question, str(r_ans)


def start_game_gcd():
    start_game(GCD_INSTRUCTION, get_math_expression_result)
