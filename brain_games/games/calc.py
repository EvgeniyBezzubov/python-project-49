from brain_games.const import calc_instruction
import random
from brain_games.engine import start_game
from brain_games.const import lst_operations
from brain_games.utils import rand_int
from brain_games.const import start_num_for_randomize_1
from brain_games.const import end_num_for_randomize_100


def return_right_ans_and_question():
    generated_random_num_1: int = rand_int(start_num_for_randomize_1,
                                           end_num_for_randomize_100)
    generated_random_num_2 = rand_int(start_num_for_randomize_1,
                                      end_num_for_randomize_100)
    rand_num_for_operation = random.randint(0, 2)
    rand_operation = lst_operations[rand_num_for_operation]
    question = f'Question: {generated_random_num_1} \
{rand_operation} {generated_random_num_2}'
    right_ans = str(eval(f"{generated_random_num_1}\
         {lst_operations[rand_operation]} {generated_random_num_2}"))
    use_opertaion_on_numbers_and_return_right_ans(
        generated_random_num_1, rand_operation, generated_random_num_2)
    return [right_ans, question]


def start_game_calc():
    start_game(calc_instruction, return_right_ans_and_question)


def use_opertaion_on_numbers_and_return_right_ans(
        generated_random_num_1,
        rand_operation,
        generated_random_num_2):
    pass
