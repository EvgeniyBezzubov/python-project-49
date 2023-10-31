import random
from brain_games.const import EVEN_INSTRUCTION
from brain_games.drive import say_hello
from brain_games.drive import user_response_request


def return_r_ans_even():
    generated_random_num = random.randint(1, 100)
    print(EVEN_INSTRUCTION)
    print('Question:', generated_random_num)
    correct_answer = get_correct_answer(generated_random_num)
    return correct_answer


def start_game_even():
    user_response_request(say_hello, return_r_ans_even)


def get_correct_answer(generated_random_num):
    if generated_random_num % 2 == 1:
        correct_answer = "no"
    else:
        correct_answer = "yes"
    return correct_answer
