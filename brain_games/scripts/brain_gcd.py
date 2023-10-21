#!/usr/bin/env python3
import brain_games.scripts.cli as cli
import games.game_gcd as drive_gcd


def main():
    name = cli.main()
    drive_gcd.run(name)


if __name__ == "__main__":
    main()
