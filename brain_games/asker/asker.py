#!usr/bin/env python3
import prompt


def ask_you(question):
    """Asking a user question and return the answer"""
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')
    return answer
