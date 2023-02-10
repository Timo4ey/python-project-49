#!usr/bin/env python3
from string import digits


def answer_loop(fn):
    def wrapper(name=''):
        counter = 0
        while counter < 3:
            res = fn(name)
            if res == 'Correct!':
                print('Correct!')
                counter += 1
                if counter == 3:
                    print(f"Congratulations, {name}")
            else:
                que = "\'" if res[0] in digits else "\""
                user_answer = f"{que}{res[0]}{que} is wrong answer ;(."
                correct_answer = f"Correct answer was {que}{res[1]}{que}."
                print(user_answer, correct_answer,
                      f"\nLet's try again, {name}!")
                break
    return wrapper
