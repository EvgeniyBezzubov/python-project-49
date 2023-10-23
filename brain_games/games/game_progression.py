#!/usr/bin/env python3
import prompt
import random
from brain_games.scripts.cli import main
from brain_games.drive import ans_validator


def run(num_correct_ans = 0 ):
    name = main()
    print("What number is missing in the progression?")
     # нужно 3 правильных ответа, не важно сколько ошибок
    while num_correct_ans < 3:
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
        ans = prompt.string('Your answer:')
        num_correct_ans = ans_validator(ans, right_ans, name, num_correct_ans)

