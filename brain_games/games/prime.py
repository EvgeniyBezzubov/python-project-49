#!/usr/bin/env python3
from brain_games.const import PRIME_INSTRUCTION, \
    START_NUM_FOR_RANDOMIZE_1, END_NUM_FOR_RANDOMIZE_20
from brain_games.engine import start_game
from brain_games.utils import rand_int


def isPrime(n):
    if n % 2 == 0:
        return n == 2
    elif n == 1:
        return False
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def return_r_ans_prime():
    RIGHT_ANS_STRING = ""
    simple = rand_int(START_NUM_FOR_RANDOMIZE_1,
                      END_NUM_FOR_RANDOMIZE_20)
    right_ans = isPrime(simple)
    question = f'Question: {simple}'
    if right_ans:
        RIGHT_ANS_STRING = "yes"
    else:
        RIGHT_ANS_STRING = "no"

    return RIGHT_ANS_STRING, question


def start_game_prime():
    start_game(PRIME_INSTRUCTION, return_r_ans_prime)
