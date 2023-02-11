#!usr/bin/env python3


def choose_quotes(data):
    que = "\"" if data[2] in ('brain_games.games.brain_even',
                              'brain_games.games.brain_prime') else "\'"
    return que


def check_value(res):
    """This function servers the
    loop_of_questions. It's react on a response and print an answer"""
    if isinstance(res, str):
        print('Correct!')
    else:
        que = choose_quotes(res)
        user_answer = f"{que}{res[0]}{que} is wrong answer ;(."
        correct_answer = f"Correct answer was {que}{res[1]}{que}."
        print(user_answer, correct_answer)


def loop_of_questions(fn):
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
                print(f"Congratulations, {name}!")
                counter += 1
            else:
                check_value(response)
                print(f"Let's try again, {name}!")
                break
    return wrapper
