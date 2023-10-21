#!/usr/bin/env python3
import brain_games.scripts.cli as cli
import games.game_prime as drive_prime


def main():
    name = cli.main()
    drive_prime.run(name)


if __name__ == "__main__":
    main()
