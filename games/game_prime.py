#!/usr/bin/env python3
import prompt
import random


def run(name):
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
        if RIGHT_ANS_STRING == ans:
            print("Your answer: {0}".format(ans))
            print("Correct!")
            num_correct_ans += 1
        else:
            print("Your answer: {0}".format(ans))
            print(f"'{ans}' is wrong answer;(.", end="")
            print(f"'Correct answer was '{RIGHT_ANS_STRING}'.")
            print("'Let's try again, {0}!".format(name))
            break

    if num_correct_ans == 3:
        print("Congratulations, {0}!".format(name))


def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n
