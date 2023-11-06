#!/usr/bin/env python3
import random
from brain_games.const import PROGRESSION_INSTRUCTION
from brain_games.drive import user_response_request


def return_r_ans_progression():
    num_step = 0
    ans_lst = []
    start_int = random.randint(1, 20)
    step_int = random.randint(1, 5)
    while num_step < 10:
        start_int += step_int
        ans_lst.append(start_int)
        num_step += 1
    hide_pos = random.randint(0, 9)
    right_ans = ans_lst[hide_pos]
    ans_lst[hide_pos] = ".."
    ans_string = ''
    for i in ans_lst:
        ans_string = ans_string + str(i) + " "
    ans_string = "Question: " + ans_string
    return [right_ans, ans_string]


def start_game_progression():
    user_response_request(PROGRESSION_INSTRUCTION, return_r_ans_progression)


if __name__ == "__main__":
    return_r_ans_progression()
