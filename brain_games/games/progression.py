#!/usr/bin/env python3
import random
from brain_games.const import PROGRESSION_INSTRUCTION
from brain_games.engine import start_game
from brain_games.utils import rand_int_1_5, rand_int_1_20


def generate_r_ans_and_question_for_progression():
    num_step = 0
    ans_lst = []
    start_int = rand_int_1_20()
    step_int = rand_int_1_5()
    while num_step < 10:
        start_int += step_int
        ans_lst.append(start_int)
        num_step += 1
    hide_pos = random.randint(0, 9)
    right_ans = str(ans_lst[hide_pos])
    ans_lst[hide_pos] = ".."
    ans_string = ''
    for i in ans_lst:
        ans_string = f"{ans_string}{str(i)} "
    ans_string = f"Question: {ans_string}"
    return right_ans, ans_string


def start_game_progression():
    start_game(PROGRESSION_INSTRUCTION, generate_r_ans_and_question_for_progression)


if __name__ == "__main__":
    generate_r_ans_and_question_for_progression()
