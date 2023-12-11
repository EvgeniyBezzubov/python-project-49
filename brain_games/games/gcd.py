import math
from brain_games.const import GCD_INSTRUCTION
from brain_games.engine import start_game
from brain_games.utils import get_random_num


def get_two_nums_and_gcd():
    num_1, num_2 = get_random_num(), get_random_num()
    question = f'{num_1} {num_2}'
    return question, str(gcd(num_1, num_2))
def gcd(num_1, num_2):
    return math.gcd(num_1, num_2)

def start_game_gcd():
    start_game(GCD_INSTRUCTION, get_two_nums_and_gcd)
