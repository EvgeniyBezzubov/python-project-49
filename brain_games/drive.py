import prompt


def user_response_request(name, get_answer_and_question):
    name = name()
    for i in range(3):
        right_ans = get_answer_and_question()
        ans = prompt.string('Your answer: ')
        if str(right_ans) == str(ans):
            print("Correct!")
        else:
            print(f"'{ans}' is wrong answer ;(.\
             Correct answer was '{right_ans}'.")
            print("Let's try again, {0}!".format(name))
            break  # Завершаем выполнение функции\
            # после неправильного ответа

        if i == 3:
            print("Congratulations, {0}!".format(name))


def say_hello():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print("Hello, {0}!".format(name))
    return name
