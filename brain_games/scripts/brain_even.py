#!/usr/bin/env python3

import prompt
from random import randint


def greeting():
    """Greeting a user and gets name"""
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name


def even_game(name):
    """Asks a user"""

    counter = 0
    attemps = 3
    print('Answer "yes" if the number is even, otherwise answer "no".')

    while counter < attemps:
        num = randint(1, 100)
        istrue = 'yes' if num % 2 == 0 else 'no'
        print(f'Question: {num}')
        answer = prompt.string('Your answer: ').lower()
        if answer == istrue:
            counter += 1
            print('Correct!')
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {istrue}.\
                    \nLet's try again, {name}!")
            break
        print(f"Congratulations, {name}")


def main():
    name = greeting()
    even_game(name)


if __name__ == '__main__':
    main()
