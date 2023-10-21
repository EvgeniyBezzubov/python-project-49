import prompt
import random


def run(name):
    NUM_CORRECT_ANS = 0  # нужно 3 правильных ответа, не важно сколько ошибок
    print("What is the result of the expression?")
    while NUM_CORRECT_ANS < 3:

        generated_random_num_1: int = random.randint(1, 100)
        generated_random_num_2 = random.randint(1, 100)
        rand_operation = random.randint(0, 2)
        lst_operations = ["+", "-", "*"]
        print(f'Question: {generated_random_num_1}', end="")
        print(f' {lst_operations[rand_operation]} {generated_random_num_2}')
        right_ans = eval(f"{generated_random_num_1}\
             {lst_operations[rand_operation]} {generated_random_num_2}")
        ans = prompt.string('Your answer:')

        if right_ans == int(ans):
            print("Correct!")
            NUM_CORRECT_ANS += 1
        else:
            print(f"'{ans}' is wrong answer ;(.", end="")
            print(f"' Correct answer was '{right_ans}'.", end="")
            print("'Let's try again, {0}!".format(name))
            break

    if NUM_CORRECT_ANS == 3:
        print("Congratulations, {0}!".format(name))
