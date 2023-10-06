#!/usr/bin/env python3
import prompt
import random
import sys
sys.path.append(r'C:\Users\user\Desktop\pythonProject\python-project-49\brain_games\scripts')
sys.path.append('/home/raindrops/.local/lib/python3.10/site-packages/brain_games/scripts/')
import cli

def main():

    name = cli.main()
    true_ans = 0
    while true_ans < 3:
        rand_int = random.randint(1, 100)
        print('Answer "yes" if the number is even, otherwise answer "no".')
        print('Question:', rand_int)
        ans = prompt.string('Your answer:')
        if rand_int % 2 == 1:
            correct_ans = "no"
        else:
            correct_ans = "yes"
        if ans == correct_ans:
            print("Correct!")
            true_ans += 1
        elif ans != correct_ans:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(ans, correct_ans))
            print("Let's try again,{0}!".format(name))
            true_ans = 0
            break
    if true_ans == 3:
        print("Congratulations, {0}!".format(name))


if __name__ == "__main__":
    main()
