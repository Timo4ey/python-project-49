#!usr/bin/env python3


def quotes(data):
    que = "\"" if data[2] == 'brain_games.games.brain_even' else "\'"
    return que


def check_value(res):
    """This function servers the
    answer_loop. It's react on a response and print an answer"""
    if isinstance(res, str):
        print('Correct!')
    else:
        que = quotes(res)
        user_answer = f"{que}{res[0]}{que} is wrong answer ;(."
        correct_answer = f"Correct answer was {que}{res[1]}{que}."
        print(user_answer, correct_answer)


def answer_loop(fn):
    """This is a decorator that call a function 3 times"""
    def wrapper(name=''):
        counter = 0
        while counter < 3:
            response = fn(name)
            if response == 'Correct!' and counter <= 1:
                check_value(response)
                counter += 1
            elif response == 'Correct!' and counter == 2:
                check_value(response)
                print(f"Congratulations, {name}")
                counter += 1
            else:
                check_value(response)
                print(f"Let's try again, {name}!")
                break
    return wrapper
