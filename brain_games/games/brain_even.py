#!/usr/bin/env python3

from random import randint
from brain_games.scripts.greeting.greeting import welcome_user
from brain_games.scripts.loop_of_questions.loop_of_questions import loop_of_questions
from brain_games.scripts.asker.asking_question import asking_question


@loop_of_questions
def even_game(name: str):
    num = randint(1, 100)
    answer = 'yes' if num % 2 == 0 else 'no'
    response = asking_question(num)
    if response == answer:
        return 'Correct!'
    else:
        return response, answer, __name__


def main():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    name = welcome_user()
    even_game(name)


if __name__ == '__main__':
    main()
