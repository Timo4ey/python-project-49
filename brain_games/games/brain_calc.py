#!usr/bin/env python3

from brain_games.scripts.create_example.create_example \
    import create_example
from brain_games.scripts.greeting.greeting import welcome_user
from brain_games.scripts.loop_of_questions.loop_of_questions \
    import loop_of_questions
from brain_games.scripts.asker.asking_question import asking_question


def calc(operand_a: int, operand_b: int, operand: str) -> int:
    operations = {"+": operand_a + operand_b,
                  "-": operand_a - operand_b,
                  "*": operand_a * operand_b}
    return operations.get(operand)


@loop_of_questions
def brain_calc(name: str) -> str | tuple:
    operand_a, operand_b, symbol = create_example()
    example = f'{operand_a} {symbol} {operand_b}'
    answer = calc(operand_a, operand_b, symbol)
    response = asking_question(example)
    if response == str(answer):
        return 'Correct!'
    else:
        return response, answer, __name__


def main():
    print("What is the result of the expression?")
    name = welcome_user()
    brain_calc(name)


if __name__ == '__main__':
    main()
