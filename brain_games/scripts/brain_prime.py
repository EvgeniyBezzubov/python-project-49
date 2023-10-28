#!/usr/bin/env python3
from brain_games.scripts.cli import hello
from brain_games.games.game_prime import game_prime_run
from brain_games.drive import ans_validator


def main():
    ans_validator(hello, game_prime_run)


if __name__ == "__main__":
    main()
