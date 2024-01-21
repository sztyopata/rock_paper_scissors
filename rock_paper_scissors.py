#!/usr/bin/python3

# My implementation of rock-paper-scissors game

from random import choice
import os


def input_validation(input: str, choices=('rock', 'paper', 'scissors')):
    if input in choices:
        return True
    return False


def display_ascii_art_for_given_choice(choice):
    # Rock Paper Scissors ASCII Art
    # Rock
    rock_ascii_art = """
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    """

    # Paper
    paper_ascii_art = """
        _______
    ---'    ____)____
            ______)
            _______)
            _______)
    ---.__________)
    """

    # Scissors
    scissors_ascii_art = """
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    """

    if choice == 'rock':
        return print(rock_ascii_art)
    
    if choice == 'paper':
        return print(paper_ascii_art)
    
    if choice == 'scissors':
        return print(scissors_ascii_art)


options = ('rock', 'paper', 'scissors')

user_wins = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}

wins = defeats = ties = 0

while True:
    if os.name == 'posix':
        os.system('clear')
    my_choice = input('Give me your choice: ').lower()
    while input_validation(my_choice) is False:
        my_choice = input('Give me your choice: ').lower()
    print(f"Your choice: {my_choice}")
    display_ascii_art_for_given_choice(my_choice)


    counter_choice = choice(options)
    print(f"Computer choice: {counter_choice}")
    display_ascii_art_for_given_choice(counter_choice)

    if user_wins[my_choice] == counter_choice:
        wins += 1
        print('Result: WIN')
    elif my_choice == counter_choice:
        ties += 1
        print('Result: TIE')
    else:
        defeats += 1
        print('Result: DEFEAT')

    want_exit = input("Another game: ").lower()[0]
    while input_validation(want_exit, choices=('y', 'n')) is False:
        want_exit = input("Another game: ").lower()[0]

    if want_exit[0] == 'n':
        print(f'Your result: {wins} win(s), {ties} tie(s), {defeats} defeat(s)')
        break



