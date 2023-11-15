#!/usr/bin/env python3
from brain_games.const import prime_instruction
from brain_games.engine import start_game
from brain_games.utils import rand_int
from brain_games.const import start_num_for_randomize_1
from brain_games.const import end_num_for_randomize_20


def return_r_ans_prime():
    RIGHT_ANS_STRING = ""
    simple = rand_int(start_num_for_randomize_1,
                      end_num_for_randomize_20)
    right_ans = isPrime(simple)
    question = f'Question: {simple}'
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
    start_game(prime_instruction, return_r_ans_prime)
