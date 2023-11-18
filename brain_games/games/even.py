from brain_games.const import EVEN_INSTRUCTION, \
    START_NUM_FOR_RANDOMIZE_1, END_NUM_FOR_RANDOMIZE_100
from brain_games.engine import start_game
from brain_games.utils import rand_int


def generate_correct_answer(generated_random_num):
    if generated_random_num % 2 == 1:
        correct_answer = "no"
    else:
        correct_answer = "yes"
    return correct_answer


def return_r_ans_and_question_even():
    generated_random_num = rand_int(START_NUM_FOR_RANDOMIZE_1,
                                    END_NUM_FOR_RANDOMIZE_100)
    question = f'Question: {generated_random_num}'
    correct_answer = str(generate_correct_answer(generated_random_num))
    return correct_answer, question


def start_game_even():
    start_game(EVEN_INSTRUCTION, return_r_ans_and_question_even)
