#!/usr/bin/env python3

from random import randint
from ..greeting import welcome_user
from brain_games.answer_loop.answer_loop import answer_loop
from brain_games.asker.asker import ask_u_str


@answer_loop
def even_game(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')

    num = randint(1, 100)
    is_true = 'yes' if num % 2 == 0 else 'no'
    answer = ask_u_str(num)
    if answer == is_true:
        return 'Correct!'
    else:
        return answer, is_true


def main():
    name = welcome_user()
    even_game(name)


if __name__ == '__main__':
    main()
