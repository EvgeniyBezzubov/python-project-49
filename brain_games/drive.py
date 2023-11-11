import prompt
from brain_games.const import NUM_OF_ROUNDS


def start_game(instruction, get_answer_and_question):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    for _ in range(NUM_OF_ROUNDS):
        right_ans, question = get_answer_and_question()
        instruction_and_end_line_and_question = instruction + "\n" + question
        print(instruction_and_end_line_and_question)
        ans = prompt.string('Your answer: ')
        if str(right_ans) == ans:
            print("Correct!")
        else:
            print(f"'{ans}' is wrong answer ;(.\
             Correct answer was '{right_ans}'.")
            print(f"Let's try again, {name}!")
            break
        if _ == 2:
            print(f"Congratulations, {name}!")
