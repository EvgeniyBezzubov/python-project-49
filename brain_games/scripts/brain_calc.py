#!/usr/bin/env python3
import prompt
import random
import brain_games.scripts.cli as cli


def main():
    NUM_CORRECT_ANS = 0  # нужно 3 правильных ответа, не важно сколько ошибок
    name = cli.main()
    print("What is the result of the expression?")
    while NUM_CORRECT_ANS < 3:

        generated_random_num_1: int = random.randint(1, 100)
        generated_random_num_2 = random.randint(1, 100)
        rand_operation = random.randint(0, 2)
        lst_operations = ["+", "-", "*"]
        print(f'Question: {generated_random_num_1} {lst_operations[rand_operation]} {generated_random_num_2}')
        right_ans = eval(f"{generated_random_num_1} {lst_operations[rand_operation]} {generated_random_num_2}")
        ans = prompt.string('Your answer:')
        try:
            if right_ans == int(ans):
                print("Correct!")
                NUM_CORRECT_ANS += 1
            else:
                print(f"'{ans}' is wrong answer ;(. Correct answer was '{right_ans}'.")
                print("'Let's try again, {0}!".format(name))
                break
        except:
            print("Ввод не верен")
            break

    if NUM_CORRECT_ANS == 3:
        print("Congratulations, {0}!".format(name))


if __name__ == "__main__":
    main()
