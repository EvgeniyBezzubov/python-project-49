#!/usr/bin/env python3
import brain_games.scripts.cli as cli
import brain_games.games.game_brain_even as drive_brain_even


def main():
    name = cli.main()
    drive_brain_even.run(str(name))


if __name__ == "__main__":
    main()
