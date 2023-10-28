import prompt


def ans_validator(name, get_answer_and_question):
    name = name()
    NUM_CORRECT_ANS = 0  # Перемещаем запрос имени пользователя в начало функции
    while NUM_CORRECT_ANS < 3:
        right_ans = get_answer_and_question()  # Вызываем функцию для получения вопроса и ответа
        ans = prompt.string('Your answer: ')
        if str(right_ans) == str(ans):
            print("Correct!")
            NUM_CORRECT_ANS += 1
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{right_ans}'.")
            print("Let's try again, {0}!".format(name))
            break  # Завершаем выполнение функции после неправильного ответа

        if NUM_CORRECT_ANS == 3:
            print("Congratulations, {0}!".format(name))
