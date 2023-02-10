#!usr/bin/env python3


def answer_loop(fn):
    def wrapper(name=''):
        counter = 0
        while counter < 3:
            func = fn(name)
            if func == 'Correct!':
                print('Correct!')
                counter += 1
                if counter == 3:
                    print(f"Congratulations, {name}")
            else:
                print(f"{func[0]} is wrong answer ;(. Correct answer was\
                 {func[1]}.\nLet's try again, {name}!")
                break
    return wrapper
