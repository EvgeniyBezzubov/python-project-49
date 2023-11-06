import random
from brain_games.const import EVEN_INSTRUCTION
from brain_games.drive import user_response_request


def return_r_ans_and_question_even():
    generated_random_num = random.randint(1, 100)
    question = 'Question:' + str(generated_random_num)
    correct_answer = is_correct_answer(generated_random_num)
    return [correct_answer, question]


def is_correct_answer(generated_random_num):
    if generated_random_num % 2 == 1:
        correct_answer = "no"
    else:
        correct_answer = "yes"
    return correct_answer


def start_game_even():
    user_response_request(EVEN_INSTRUCTION, return_r_ans_and_question_even)
