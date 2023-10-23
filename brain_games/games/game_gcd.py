import prompt
import random
import math
from brain_games.drive import ans_validator
from brain_games.scripts.cli import main

def run(NUM_CORRECT_ANS = 0):
    name = main()
    print("Find the greatest common divisor of given numbers.")
    while NUM_CORRECT_ANS < 3:
        generated_random_num_1: int = random.randint(1, 100)
        generated_random_num_2 = random.randint(1, 100)
        print(f'Question: {generated_random_num_1} {generated_random_num_2} ')
        r_ans = math.gcd(generated_random_num_1, generated_random_num_2)
        ans = prompt.string('Your answer:')
        NUM_CORRECT_ANS = ans_validator(ans, r_ans, name, NUM_CORRECT_ANS)
