#!usr/bin/env python3

from random import randint, choice


def create_example() -> tuple:
    operators = ['+', '-', '*']
    operand_a = randint(1, 100)
    operand_b = randint(1, 100)
    symbol = choice(operators)
    return operand_a, operand_b, symbol