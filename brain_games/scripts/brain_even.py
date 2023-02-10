#!/usr/bin/env python3

from random import randint
from brain_games.greeting.greeting import welcome_user
from brain_games.answer_loop.answer_loop import answer_loop
from brain_games.asker.asker import ask_you


@answer_loop
def even_game(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')

    num = randint(1, 100)
    answer = 'yes' if num % 2 == 0 else 'no'
    response = ask_you(num)
    if response == answer:
        return 'Correct!'
    else:
        return response, answer


def main():
    name = welcome_user()
    even_game(name)


if __name__ == '__main__':
    main()
