#!/usr/bin/env python3
import prompt
import random
import sys

sys.path.append(r'C:\Users\user\Desktop\pythonProject\python-project-49\brain_games\scripts')
sys.path.append('/home/raindrops/.local/lib/python3.10/site-packages/brain_games/scripts/')
import cli
import math


def main():
    NUM_CORRECT_ANS = 0  # нужно 3 правильных ответа, не важно сколько ошибок
    name = cli.main()
    print("Find the greatest common divisor of given numbers.")
    while NUM_CORRECT_ANS < 3:
        generated_random_num_1 = random.randint(1, 100)
        generated_random_num_2 = random.randint(1, 100)
        print('Question: {0} {1} '.format(generated_random_num_1, generated_random_num_2))
        right_ans = math.gcd(generated_random_num_1, generated_random_num_2)
        ans = prompt.string('Your answer:')
        try:
            if right_ans == int(ans):
                print("Correct!")
                NUM_CORRECT_ANS += 1
            else:
                print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(ans, right_ans))
                print("'Let's try again, {0}!".format(name))
                break
        except:
            print("Ввод не верен")
            break

    if NUM_CORRECT_ANS == 3:
        print("Congratulations, {0}!".format(name))
if __name__ == "__main__":
    main()
