#!/usr/bin/env python3
import prompt
import random
import sys
sys.path.append(r'C:\Users\user\Desktop\pythonProject\python-project-49\brain_games\scripts')
sys.path.append('/home/raindrops/.local/lib/python3.10/site-packages/brain_games/scripts/')
import cli


def main():
    name = cli.main()
    num_correct_ans = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    while num_correct_ans < 3:
        RIGHT_ANS_STRING = ""
        simple = random.randint(1, 20)
        right_ans = isPrime(simple)
        print('Question: {0}'.format(simple))
        if right_ans == True:
            RIGHT_ANS_STRING = "yes"
        else:
            RIGHT_ANS_STRING = "no"

        ans = prompt.string('Your answer:')
        if RIGHT_ANS_STRING == ans:
            print("Your answer: {0}".format(ans))
            print("Correct!")
            num_correct_ans+=1
        else:
            print("Your answer: {0}".format(ans))
            print("'{0}' is wrong answer;(.Correct answer was '{1}'.".format(ans, right_ans_string))
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


if __name__ == "__main__":
    main()
