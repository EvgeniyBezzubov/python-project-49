import prompt
from brain_games.const import NUM_OF_ROUNDS


def start_game(instruction, get_answer_and_question):
    user_name = prompt.string("Welcome to the Brain Games!\n May I have your name?")
    print(f"Hello, {user_name}! \ninstruction")
    for _ in range(NUM_OF_ROUNDS):
        right_ans, question = get_answer_and_question()
        user_ans = prompt.string(f'{question}\nYour answer: ')
        if right_ans == user_ans:
            print("Correct!")
        else:
            print(f"'{user_ans}' is wrong answer ;(.\
             \nCorrect answer was '{right_ans}'.\
             \nLet's try again, {user_name}!")
            return
    print(f"Congratulations, {user_name}!")
