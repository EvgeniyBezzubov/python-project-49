#!/usr/bin/env python3
import prompt
import random
import sys
sys.path.append(r'C:\Users\user\Desktop\pythonProject\python-project-49\brain_games\scripts')
sys.path.append(r'/home/raindrops/python-project-49/brain_games/scripts')
import cli

def main():
    num_correct_ans = 0 #нужно 3 правильных ответа, не важно сколько ошибок
    name = cli.main()
    print("What is the result of the expression?")
    while num_correct_ans <3:

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
                print("'Let's try again, {0}!".format(name))

        except:
            print("Ввод не верен")
if __name__ == "__main__":
    main()
