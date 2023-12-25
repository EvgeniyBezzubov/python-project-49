from brain_games.const import PROGRESSION_INSTRUCTION, PROGRESSION_LENGTH
from brain_games.engine import start_game
from brain_games.utils import get_random_num


def get_progression_and_hidden_num():
    start, step = get_random_num(1, 20), get_random_num(1, 20)
    progression = generate_progression(start, step, PROGRESSION_LENGTH)
    hidden_index = get_random_num(0, PROGRESSION_LENGTH - 1)
    hidden_num = progression[hidden_index]
    progression[hidden_index] = '..'
    pg_with_hidden_num = ' '.join(map(str, progression))
    return pg_with_hidden_num, str(hidden_num)


def generate_progression(start, step, length):
    return [start + step * i for i in range(length)]


def start_game_progression():
    start_game(PROGRESSION_INSTRUCTION, get_progression_and_hidden_num)
