from brain_games.games.game_cli import say_hello


def hello():
    name = say_hello()
    return name


if __name__ == "__main__":
    hello()
