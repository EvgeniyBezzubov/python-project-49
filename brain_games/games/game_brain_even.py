import random
from brain_games.const import EVEN_INSTRUCTION
from brain_games.drive import ans_validator
from brain_games.scripts.cli import hello


def game_even_run():

    generated_random_num = random.randint(1, 100)
    print(EVEN_INSTRUCTION)
    print('Question:', generated_random_num)
    if generated_random_num % 2 == 1:
        correct_answer = "no"
    else:
        correct_answer = "yes"

    return correct_answer
def start_game_even_one_line():
    ans_validator(hello, game_even_run)