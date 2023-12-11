#!/usr/bin/env python3
from brain_games.const import PRIME_INSTRUCTION
from brain_games.engine import start_game
from brain_games.utils import get_random_num


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
    simple = get_random_num(1, 20)
    question = f'{simple}'
    RIGHT_ANS_STRING = 'yes' if isPrime(simple) else 'no'
    return question, RIGHT_ANS_STRING


def start_game_prime():
    start_game(PRIME_INSTRUCTION, get_math_expression_result)
