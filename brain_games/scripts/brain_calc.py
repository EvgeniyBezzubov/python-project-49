#!/usr/bin/env python3
import prompt
import random


def main():
    num_correct_ans = 0 #нужно 3 правильных ответа, не важно сколько ошибок
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print("Hello, {0}!".format(name))
    print("What is the result of the expression?")
    while num_correct_ans <1:

        rand_int_a = random.randint(1, 100)
        rand_int_b = random.randint(1, 100)
        rand_operation = random.randint(0, 2)
        lst_operations =["+", "-","*"]
        print('Question: {0} {1} {2}'.format(rand_int_a, lst_operations[rand_operation], rand_int_b) )
        right_ans = eval("{0} {1} {2}".format(rand_int_a, lst_operations[rand_operation], rand_int_b))
        ans = prompt.string('Your answer:')
        try:
            if right_ans == int(ans):
                print("Correct!")
                num_correct_ans+=1
            else:
                print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(ans, right_ans))
        except:
            print("Ввод не верен")
if __name__ == "__main__":
    main()
