import random
import math
from brain_games.const import GCD_INSTRUCTION
from brain_games.scripts.cli import hello
from brain_games.drive import ans_validator


def game_gcd_run():
    print(GCD_INSTRUCTION)
    generated_random_num_1: int = random.randint(1, 100)
    generated_random_num_2 = random.randint(1, 100)
    print(f'Question: {generated_random_num_1} {generated_random_num_2} ')
    r_ans = math.gcd(generated_random_num_1, generated_random_num_2)
    return r_ans


def start_game_gcd_one_line():
    ans_validator(hello, game_gcd_run)
