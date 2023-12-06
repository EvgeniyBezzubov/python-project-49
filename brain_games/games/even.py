from brain_games.const import EVEN_INSTRUCTION
from brain_games.engine import start_game
from brain_games.utils import rand


def generate_correct_answer(num):
    if num % 2 == 1:
        correct_answer = "no"
    else:
        correct_answer = "yes"
    return correct_answer


def get_math_expression_result():
    generated_random_num = rand()
    question = f'{generated_random_num}'
    correct_answer = generate_correct_answer(generated_random_num)
    return question, str(correct_answer)


def start_game_even():
    start_game(EVEN_INSTRUCTION, get_math_expression_result)
