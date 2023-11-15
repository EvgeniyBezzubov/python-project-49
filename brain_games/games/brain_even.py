import random
from brain_games.const import even_instruction
from brain_games.engine import start_game
from brain_games.utils import rand_int
from brain_games.const import start_num_for_randomize_1
from brain_games.const import end_num_for_randomize_100


def return_r_ans_and_question_even():
    generated_random_num = rand_int(start_num_for_randomize_1, end_num_for_randomize_100)
    question = f'Question: {generated_random_num}'
    correct_answer = str(is_correct_answer(generated_random_num))
    return [correct_answer, question]


def is_correct_answer(generated_random_num):
    if generated_random_num % 2 == 1:
        correct_answer = "no"
    else:
        correct_answer = "yes"
    return correct_answer


def start_game_even():
    start_game(even_instruction, return_r_ans_and_question_even)
