#!/usr/bin/env python3
import prompt
import random
import brain_games.scripts.cli as cli
import math


def main():
    NUM_CORRECT_ANS = 0  # нужно 3 правильных ответа, не важно сколько ошибок
    name = cli.main()
    print("Find the greatest common divisor of given numbers.")
    while NUM_CORRECT_ANS < 3:
        generated_random_num_1: int = random.randint(1, 100)
        generated_random_num_2 = random.randint(1, 100)
        print(f'Question: {generated_random_num_1} {generated_random_num_2} ')
        r_ans = math.gcd(generated_random_num_1, generated_random_num_2)
        ans = prompt.string('Your answer:')

        if r_ans == int(ans):
            print("Correct!")
            NUM_CORRECT_ANS += 1
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{r_ans}'.")
            print("'Let's try again, {0}!".format(name))
            break

    if NUM_CORRECT_ANS == 3:
        print("Congratulations, {0}!".format(name))


if __name__ == "__main__":
    main()
