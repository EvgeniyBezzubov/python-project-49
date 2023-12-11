#!/usr/bin/env python3
import random
from brain_games.const import PROGRESSION_INSTRUCTION
from brain_games.engine import start_game
from brain_games.utils import get_random_num


def get_math_expression_result():
    ans_lst = generate_list_progression()
    hide_pos = random.randint(0, 9)
    right_ans = ans_lst[hide_pos]
    ans_lst[hide_pos] = ".."
    ans_string = ''
    for i in ans_lst:
        ans_string = f"{ans_string}{str(i)} "
    ans_string = f"{ans_string}"
    return ans_string, str(right_ans)


def generate_list_progression():
    num_step = 0
    ans_lst = []
    start_int = get_random_num(1, 20)
    step_int = get_random_num(1, 5)
    while num_step < 10:
        start_int += step_int
        ans_lst.append(start_int)
        num_step += 1
    return ans_lst


def start_game_progression():
    start_game(PROGRESSION_INSTRUCTION,
               get_math_expression_result)
