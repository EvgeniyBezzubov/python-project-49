#!/usr/bin/env python3
import random
from brain_games.const import progression_instruction
from brain_games.engine import start_game
from brain_games.utils import rand_int
from brain_games.const import start_num_for_randomize_1
from brain_games.const import end_num_for_randomize_5
from brain_games.const import end_num_for_randomize_20


def return_right_ans_and_question():
    num_step = 0
    ans_lst = []
    start_int = rand_int(start_num_for_randomize_1, end_num_for_randomize_20)
    step_int = rand_int(start_num_for_randomize_1, end_num_for_randomize_5)
    while num_step < 10:
        start_int += step_int
        ans_lst.append(start_int)
        num_step += 1
    hide_pos = random.randint(0, 9)
    right_ans = str(ans_lst[hide_pos])
    ans_lst[hide_pos] = ".."
    ans_string = ''
    for i in ans_lst:
        ans_string = ans_string + str(i) + " "
    ans_string = f"Question: {ans_string}"
    return right_ans, ans_string


def start_game_progression():
    start_game(progression_instruction, return_right_ans_and_question)


if __name__ == "__main__":
    return_right_ans_and_question()
