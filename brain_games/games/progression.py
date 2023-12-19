from brain_games.const import PROGRESSION_INSTRUCTION, PROGRESSION_LENGTH
from brain_games.engine import start_game
from brain_games.utils import get_random_num

#чего уж мелочиться
def get_progression_and_hidden_num():  # изменил название - на соответсвующее
    start, step = get_random_num(1, 20), get_random_num(1, 20)
    progression = generate_progression(start, step, PROGRESSION_LENGTH)
    hidden_index = get_random_num(0, PROGRESSION_LENGTH - 1)  #  вся логика начинается тут
    hidden_num = progression[hidden_index]
    progression[hidden_index] = '..'
    pg_with_hidden_num = ' '.join(map(str, progression))
    return pg_with_hidden_num, str(hidden_num)


# Это не чистно давать задания по 1 му модулю, ответы на которые берут из 2 го модуля
def generate_progression(start, step, length):
    return [start + step * i for i in range(length)]


def start_game_progression():
    start_game(PROGRESSION_INSTRUCTION,
               get_progression_and_hidden_num)
