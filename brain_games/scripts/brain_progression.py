#!/usr/bin/env python3
import prompt
import random
import brain_games.scripts.cli as cli


def main():
    num_correct_ans = 0  # нужно 3 правильных ответа, не важно сколько ошибок
    name = cli.main()
    print("What number is missing in the progression?")

    while num_correct_ans < 3:
        num_step = 0
        ans_lst = []
        start_int = random.randint(1, 20)
        step_int = random.randint(1, 5)
        while num_step < 10:
            start_int += step_int
            ans_lst.append(start_int)
            num_step += 1
        hide_pos = random.randint(0, 9)
        right_ans = ans_lst[hide_pos]
        ans_lst[hide_pos] = ".."
        ans_string = ''
        for i in ans_lst:
            ans_string = ans_string + str(i) + " "
        ans_string = "Question: " + ans_string
        print(ans_string)
        ans = prompt.string('Your answer:')
        if right_ans == int(ans):
            print("Correct!")
            num_correct_ans += 1
        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(ans, right_ans))
            print("'Let's try again, {0}!".format(name))
            break

        if num_correct_ans == 3:
            print("Congratulations, {0}!".format(name))


if __name__ == "__main__":
    main()
