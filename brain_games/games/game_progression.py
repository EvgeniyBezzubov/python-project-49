#!/usr/bin/env python3
import random
from brain_games.const import PROGRESSION_INSTRUCTION
from brain_games.drive import ans_validator
from brain_games.scripts.cli import hello


def game_progression_run():
    print(PROGRESSION_INSTRUCTION)
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
    print(ans_string)
    return right_ans

def start_game_progression_one_line():
    ans_validator(hello, game_progression_run)

if __name__ == "__main__":
    game_progression_run()
