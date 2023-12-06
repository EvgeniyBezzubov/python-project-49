#!/usr/bin/env python3
from brain_games.const import PRIME_INSTRUCTION
from brain_games.engine import start_game
from brain_games.utils import rand


def isPrime(n):
    if n % 2 == 0:
        return n == 2
    elif n == 1:
        return False
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def get_math_expression_result():
    RIGHT_ANS_STRING = ""
    simple = rand(1, 20)
    right_ans = isPrime(simple)
    question = f'{simple}'
    if right_ans:
        RIGHT_ANS_STRING = "yes"
    else:
        RIGHT_ANS_STRING = "no"

    return question, RIGHT_ANS_STRING


def start_game_prime():
    start_game(PRIME_INSTRUCTION, get_math_expression_result)
