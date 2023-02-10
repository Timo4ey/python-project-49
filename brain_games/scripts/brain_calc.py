#!usr/bin/env python3

from random import randint, choice
from brain_games.greeting.greeting import welcome_user
from brain_games.answer_loop.answer_loop import answer_loop
from brain_games.asker.asker import ask_you


def calc(operand_a: int, operand_b: int, operand: str) -> int:
    operations = {"+": operand_a + operand_b,
                  "-": operand_a - operand_b,
                  "*": operand_a * operand_b}
    return operations.get(operand)


def create_example() -> tuple:
    operators = ['+', '-', '*']
    operand_a = randint(1, 100)
    operand_b = randint(1, 100)
    symbol = choice(operators)
    return operand_a, operand_b, symbol


@answer_loop
def brain_calc(name: str) -> str | tuple:
    operand_a, operand_b, symbol = create_example()
    example = f'{operand_a} {symbol} {operand_b}'
    answer = calc(operand_a, operand_b, symbol)
    response = ask_you(example)
    if response == str(answer):
        return 'Correct!'
    else:
        return response, answer


def main():
    print("What is the result of the expression?")
    name = welcome_user()
    brain_calc(name)


if __name__ == '__main__':
    main()
