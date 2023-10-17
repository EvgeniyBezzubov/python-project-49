#!/usr/bin/env python3
import prompt
import random
import brain_games.scripts.cli as cli


def main():
    name = cli.main()
    COUNT_TRUE_ANS = 0
    while COUNT_TRUE_ANS < 3:
        generated_random_num = random.randint(1, 100)
        print('Answer "yes" if the number is even, otherwise answer "no".')
        print('Question:', generated_random_num)
        user_answer = prompt.string('Your answer:')
        if generated_random_num % 2 == 1:
            correct_answer = "no"
        else:
            correct_answer = "yes"
        if user_answer == correct_answer:
            print("Correct!")
            COUNT_TRUE_ANS += 1
        elif user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(.", end="")
            print(f"' Correct answer was '{correct_answer}'.", end="")
            print("Let's try again, {0}!".format(name))
            COUNT_TRUE_ANS = 0
            break
    if COUNT_TRUE_ANS == 3:
        print("Congratulations, {0}!".format(name))


if __name__ == "__main__":
    main()
