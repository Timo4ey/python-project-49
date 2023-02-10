#!usr/bin/env python3


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
                user_answer = f"\"{res[0]}\" is wrong answer ;(."
                correct_answer = f"Correct answer was \"{res[1]}\"."
                print(user_answer, correct_answer,
                      f"\nLet's try again, {name}!")
                break
    return wrapper
