#!usr/bin/env python3
from string import digits


def check_value(res):
    if isinstance(res, str):
        print('Correct!')
    else:
        que = "\'" if res[0] in digits else "\""
        user_answer = f"{que}{res[0]}{que} is wrong answer ;(."
        correct_answer = f"Correct answer was {que}{res[1]}{que}."
        print(user_answer, correct_answer)


def answer_loop(fn):
    def wrapper(name=''):
        counter = 0
        while counter < 3:
            res = fn(name)
            if res == 'Correct!':
                check_value(res)
                counter += 1
                if counter == 3:
                    print(f"Congratulations, {name}")
            else:
                check_value(res)
                print(f"Let's try again, {name}!")
                break
    return wrapper
