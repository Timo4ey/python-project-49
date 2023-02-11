from math import sqrt
from brain_games.scripts.create_example.create_example import create_example
from brain_games.scripts.greeting.greeting import welcome_user
from brain_games.scripts.loop_of_questions.loop_of_questions import loop_of_questions
from brain_games.scripts.asker.asking_question import asking_question


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


@loop_of_questions
def brain_prime(name: str):
    gen_num, _, _ = create_example()
    answer = define_simple_numbers(gen_num)
    response = asking_question(gen_num)
    if response == str(answer):
        return 'Correct!'
    else:
        return response, answer, __name__


def main():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    name = welcome_user()
    brain_prime(name)


if __name__ == '__main__':
    main()
