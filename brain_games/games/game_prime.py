#!/usr/bin/env python3
import prompt
import random
from brain_games.scripts.cli import main
from brain_games.drive import ans_validator


def run(num_correct_ans=0):
    name = main()
    num_correct_ans = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while num_correct_ans < 3:
        RIGHT_ANS_STRING = ""
        simple = random.randint(1, 20)
        right_ans = isPrime(simple)
        print('Question: {0}'.format(simple))
        if right_ans:
            RIGHT_ANS_STRING = "yes"
        else:
            RIGHT_ANS_STRING = "no"

        ans = prompt.string('Your answer:')
        num_correct_ans = ans_validator(ans, RIGHT_ANS_STRING, name, num_correct_ans)


def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n
