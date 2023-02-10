#!usr/bin/env python3
import prompt


def ask_u_str(question):
    """Askign a user question and return the unswer"""
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')
    return answer
