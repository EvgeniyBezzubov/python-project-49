from brain_games.const import EVEN_INSTRUCTION
from brain_games.engine import start_game
from brain_games.utils import get_random_num


def is_even(num):  # Вот же тернарный оператор(вычисления???)
    return ("no", "yes")[num % 2 == 0]


def get_num_and_even_ans():
    num = get_random_num()
    return num, is_even(num)


def start_game_even():
    start_game(EVEN_INSTRUCTION, get_num_and_even_ans)
