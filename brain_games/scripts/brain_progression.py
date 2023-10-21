#!/usr/bin/env python3
import games.game_progression as drive_progression
import brain_games.scripts.cli as cli


def main():
    name = cli.main()
    drive_progression.run(name)


if __name__ == "__main__":
    main()
