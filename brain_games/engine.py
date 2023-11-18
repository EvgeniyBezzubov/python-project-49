import prompt
from brain_games.const import NUM_OF_ROUNDS


def start_game(instruction, get_answer_and_question):
    name = prompt.string("Welcome to the Brain Games!\n May I have your name?")
    print(f"Hello, {name}!")
    print(instruction)
    for _ in range(NUM_OF_ROUNDS):
        right_ans, question = get_answer_and_question()
        print(question)
        ans = prompt.string('Your answer: ')
        if right_ans == ans:
            print("Correct!")
        else:
            print(f"'{ans}' is wrong answer ;(.\
             \nCorrect answer was '{right_ans}'.\
             \nLet's try again, {name}!")
            break
    #  if _ == 2: без данного условия, о котором вы писали
    #  код не работает корректно и пишет поздравлиения
    #  в случае неправльного ответа
    print(f"Congratulations, {name}!")
