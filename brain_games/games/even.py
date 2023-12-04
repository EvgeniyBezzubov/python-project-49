from brain_games.const import EVEN_INSTRUCTION
from brain_games.engine import start_game
from brain_games.utils import rand_1_100


def generate_correct_answer(num):
    if num % 2 == 1:
        correct_answer = "no"
    else:
        correct_answer = "yes"
    return correct_answer


def generate_math_func_and_result_even():
    generated_random_num = rand_1_100()
    question = f'Question: {generated_random_num}'
    correct_answer = str(generate_correct_answer(generated_random_num))
    return correct_answer, question


def start_game_even():
    start_game(EVEN_INSTRUCTION, generate_math_func_and_result_even)
