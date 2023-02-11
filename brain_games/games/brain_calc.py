#!usr/bin/env python3

from brain_games.scripts.create_example.create_example import create_example
from brain_games.scripts.greeting.greeting import welcome_user
from brain_games.scripts.answer_loop.answer_loop import answer_loop
from brain_games.scripts.asker.asker import ask_you


def calc(operand_a: int, operand_b: int, operand: str) -> int:
    operations = {"+": operand_a + operand_b,
                  "-": operand_a - operand_b,
                  "*": operand_a * operand_b}
    return operations.get(operand)


@answer_loop
def brain_calc(name: str) -> str | tuple:
    operand_a, operand_b, symbol = create_example()
    example = f'{operand_a} {symbol} {operand_b}'
    answer = calc(operand_a, operand_b, symbol)
    response = ask_you(example)
    if response == str(answer):
        return 'Correct!'
    else:
        return response, answer, __name__


def main():
    name = welcome_user()
    print("What is the result of the expression?")
    brain_calc(name)


if __name__ == '__main__':
    main()
