import prompt
import random

def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print("Hello, {0}!".format(name))
    print("Answer '"'yes'"' if the number is even, otherwise answer '"'no'"'.")
    return name
if __name__ == "__main__":
    main()
