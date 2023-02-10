#!/usr/bin/env python3

import prompt


def welcome_user():
    """Greeting a user and gets name"""
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name
