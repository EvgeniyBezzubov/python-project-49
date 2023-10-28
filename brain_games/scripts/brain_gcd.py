#!/usr/bin/env python3
from brain_games.games.game_gcd import game_gcd_run
from brain_games.drive import ans_validator
from brain_games.scripts.cli import hello


def main():
    ans_validator(hello, game_gcd_run)


if __name__ == "__main__":
    main()
