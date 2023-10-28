import random
import math
from brain_games.const import GCD_INSTRUCTION


def game_gcd_run():
    print(GCD_INSTRUCTION)
    generated_random_num_1: int = random.randint(1, 100)
    generated_random_num_2 = random.randint(1, 100)
    print(f'Question: {generated_random_num_1} {generated_random_num_2} ')
    r_ans = math.gcd(generated_random_num_1, generated_random_num_2)
    return r_ans
