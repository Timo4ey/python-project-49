#!/usr/bin/env python3

from random import randint
from ..greeting import welcome_user
from ..answer_loop import answer_loop
from ..ascker import ask_u_str


@answer_loop
def even_game(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')

    num = randint(1, 100)
    istrue = 'yes' if num % 2 == 0 else 'no'
    answer = ask_u_str(num)
    if answer == istrue:
        return 'Correct!'
    else:
        return answer, istrue


def main():
    name = welcome_user()
    even_game(name)


if __name__ == '__main__':
    main()
