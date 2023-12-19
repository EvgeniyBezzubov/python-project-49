from brain_games.const import PRIME_INSTRUCTION
from brain_games.engine import start_game
from brain_games.utils import get_random_num


def is_prime(n):
    if n < 2:
        return False
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def get_num_and_yes_no_string():
    num = get_random_num(1, 20)
    yes_no_string = 'yes' if is_prime(num) else 'no'
    return str(num), yes_no_string


def start_game_prime():
    start_game(PRIME_INSTRUCTION, get_num_and_yes_no_string)
