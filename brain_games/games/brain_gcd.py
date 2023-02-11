from brain_games.scripts.create_example.create_example import create_example
from brain_games.scripts.loop_of_questions.loop_of_questions import loop_of_questions
from brain_games.scripts.asker.asking_question import asking_question
from brain_games.scripts.greeting.greeting import welcome_user


def nod(operand_a, operand_b):
    if operand_a < operand_b:
        operand_a, operand_b = operand_b, operand_a
    while operand_a % operand_b != 0:
        operand_a, operand_b = operand_b, operand_a % operand_b
    return operand_b


@loop_of_questions
def brain_gcd(name: str):
    operand_1, operand_2, _ = create_example()
    response = asking_question(f"{operand_1} {operand_2}")
    answer = nod(operand_1, operand_2)
    if response == str(answer):
        return 'Correct!'
    else:
        return response, answer, __name__


def main():
    print("Find the greatest common divisor of given numbers.")
    name = welcome_user()
    brain_gcd(name)


if __name__ == '__main__':
    main()
