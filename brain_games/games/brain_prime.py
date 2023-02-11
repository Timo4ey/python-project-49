from math import sqrt
from brain_games.scripts.create_example.create_example import create_example
from brain_games.scripts.greeting.greeting import welcome_user
from brain_games.scripts.answer_loop.answer_loop import answer_loop
from brain_games.scripts.asker.asker import ask_you


def define_simple_numbers(num: int) -> str:
    i = 2
    # if i not bigger or equal square root of
    # num we start or continue the cycle
    # because square root of num should be
    # the highest number that we can division the number
    while i <= sqrt(num):
        # if the remainder of the division equal zero the num is Complex
        if num % i == 0:
            return "no"  # Complex
        # if the reminder of the division isn't equal zero than 'i' = 'i' + 1
        i += 1
    # if 'i' bigger than square root of num that means the number is Simple
    return "yes"  # Simple


@answer_loop
def brain_prime(name: str):
    gen_num, _, _ = create_example()
    answer = define_simple_numbers(gen_num)
    response = ask_you(gen_num)
    if response == str(answer):
        return 'Correct!'
    else:
        return response, answer, __name__


def main():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    brain_prime(name)


if __name__ == '__main__':
    main()
