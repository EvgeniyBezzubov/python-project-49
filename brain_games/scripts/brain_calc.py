#!/usr/bin/env python3
import brain_games.scripts.cli as cli
import games.game_calc as drive_calc


def main():
    name = cli.main()
    drive_calc.run(name)


if __name__ == "__main__":
    main()
