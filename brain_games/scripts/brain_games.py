#!/usr/bin/env python3
import prompt
import sys
sys.path.append(r'C:\Users\user\Desktop\pythonProject\python-project-49\brain_games\scripts')
sys.path.append('/home/raindrops/.local/lib/python3.10/site-packages/brain_games/scripts/')
from cli import main


def base():
    name = main()

    print()


if __name__ == "__main__":
    base()
