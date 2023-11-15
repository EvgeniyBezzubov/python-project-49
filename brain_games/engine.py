import prompt
from brain_games.const import NUM_OF_ROUNDS


def start_game(instruction, get_answer_and_question):
    name = prompt.string("Welcome to the Brain Games!\n May I have your name?")
    print(f"Hello, {name}!")
    for _ in range(NUM_OF_ROUNDS):
        right_ans, question = get_answer_and_question()
        instruction_and_end_line_and_question = instruction + "\n" + question
        print(instruction_and_end_line_and_question)
        ans = prompt.string('Your answer: ')
        if right_ans == ans:
            print("Correct!")
        else:
            print(f"'{ans}' is wrong answer ;(.\
             \nCorrect answer was '{right_ans}'.\
             \nLet's try again, {name}!")
            break
        if _ == 2:  # зачем тут данное условие? ведь мы и так выйдем из цикла после 3х успешных ответах
                    #Если убрать условие, тополучится то что на фото
                    # https://drive.google.com/file/d/1e7b2HF8WeZC46ZgKEVXTmWo7K2iHXhCC/view?usp=sharing
            print(f"Congratulations, {name}!")

