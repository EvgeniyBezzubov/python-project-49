import prompt
from brain_games.const import MAX_CORRECT_ANS


def start_some_game(instruction, get_answer_and_question):
    name = say_hello()
    for _ in range(MAX_CORRECT_ANS):
        lst_correct_ans_and_quest = get_answer_and_question()
        right_ans = lst_correct_ans_and_quest[0]
        question = lst_correct_ans_and_quest[1]
        print(instruction)
        print(question)
        ans = prompt.string('Your answer: ')
        if str(right_ans) == ans:
            print("Correct!")
        else:
            print(f"'{ans}' is wrong answer ;(.\
             Correct answer was '{right_ans}'.")
            print("Let's try again, {0}!".format(name))
            break  # Завершаем выполнение функции\
            # после неправильного ответа

        if _ == 2:
            print("Congratulations, {0}!".format(name))


def say_hello():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print("Hello, {0}!".format(name))
    return name
