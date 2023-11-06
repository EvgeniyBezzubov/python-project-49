#!/usr/bin/env python3
import random
from brain_games.const import PRIME_INSTRUCTION
from brain_games.drive import user_response_request


def return_r_ans_prime():
    RIGHT_ANS_STRING = ""
    simple = random.randint(1, 20)
    right_ans = isPrime(simple)
    question = 'Question: {0}'.format(simple)
    if right_ans:
        RIGHT_ANS_STRING = "yes"
    else:
        RIGHT_ANS_STRING = "no"

    return [RIGHT_ANS_STRING, question]


def isPrime(n):
    if n % 2 == 0:
        return n == 2
    elif n == 1:
        return False
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def start_game_prime():
    user_response_request(PRIME_INSTRUCTION, return_r_ans_prime)
