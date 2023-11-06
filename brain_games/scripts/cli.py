from brain_games.games.cli import welcome_user


def hello():
    name = welcome_user()
    return name


if __name__ == "__main__":
    hello()
