#!usr/bin/env python3
import prompt


def ask_u_str(question):
    """Asking a user question and return the answer"""
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')
    return answer
