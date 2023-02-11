from random import randint
from brain_games.scripts.loop_of_questions.loop_of_questions \
    import loop_of_questions
from brain_games.scripts.asker.asking_question import asking_question
from brain_games.scripts.greeting.greeting import welcome_user


def create_progression() -> list[int, ...]:
    gen_list = []
    while len(gen_list) < 5:
        start = randint(1, 50)
        step = randint(1, 50)
        length = randint(5, 500)
        if step <= length or length < start:
            length += step * 2

        gen_list = [x for x in range(start, length, step)]
    return gen_list if len(gen_list) <= 10 else gen_list[:10]


def riddle_progressive(progressive: list | tuple | set) -> tuple:
    choose_index = randint(0, len(progressive) - 1)
    secret_num = progressive[choose_index]
    progressive[choose_index] = '..'
    output = ' '.join([f'{x}' for x in progressive])
    return output, secret_num


@loop_of_questions
def brain_progression(name: str):
    progressive = create_progression()
    riddle, answer = riddle_progressive(progressive)
    response = asking_question(riddle)
    if response == str(answer):
        return 'Correct!'
    else:
        return response, answer, __name__


def main():
    print("What number is missing in the progression?")
    name = welcome_user()
    brain_progression(name)


if __name__ == "__main__":
    main()
