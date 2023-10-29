#!/usr/bin/env python3
import random
from brain_games.const import PRIME_INSTRUCTION
from brain_games.drive import ans_validator
from brain_games.scripts.cli import hello


def game_prime_run():
    print(PRIME_INSTRUCTION)
    RIGHT_ANS_STRING = ""
    simple = random.randint(1, 20)
    right_ans = isPrime(simple)
    print('Question: {0}'.format(simple))
    if right_ans:
        RIGHT_ANS_STRING = "yes"
    else:
        RIGHT_ANS_STRING = "no"

    return RIGHT_ANS_STRING


def isPrime(n):
    if n % 2 == 0:
        return n == 2
    elif n == 1:
        return False
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def start_game_prime_one_line():
    ans_validator(hello, game_prime_run)
