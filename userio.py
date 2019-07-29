import time
from os import system

from board import Board


def print_winner(winner: str):
    """Prints the winner, or draw"""
    winner_string = '\'' + str(winner) + '\' won.'
    draw = "The game ended in a draw."
    delimiter = "*******************************************"

    s = winner_string if winner == 'X' or winner == 'O' else draw
    print('')
    print(delimiter)
    print(s)
    print(delimiter)
    print('')


def get_number() -> int:
    """Gets number from user input"""
    while True:
        try:
            return int(input())
        except ValueError:
            print("Input could not be read. Please enter a number.")


def play_again() -> bool:
    """Asks if the player wants to play again"""
    again = ''
    while again != 'y' and again != 'n':
        again = input("Do you want to play again?[yes/no]\n").strip().lower()[0]
    return again == 'y'


def greeting() -> int:
    """Gets the player decision whether to play alone or together"""

    strings = ["Welcome", "To a game of Tic-Tac-toe", "First things first."]
    for s in strings:
        print(s)
        time.sleep(1)
    print(
        "Do you want play together, or alone against the frustrating AI? (Enter '1' or '2' for number of players): ")

    while True:
        number = get_number()
        if number == 1 or number == 2:
            break
        print("Please enter '1' to play against the Computer or '2' if you play with a friend.")

    print("If you want to quit please enter '0', when prompted to check a field.")
    return number - 1


def draw_field(field: list):
    """Prints out a representation of the field to the terminal"""
    system('clear')
    field = field[:]
    separator = "-------+-------+-------"
    between_sep = "       |       |       "
    values = "   {0}   |   {1}   |   {2}   "

    for i in range(11):
        if (i % 4) == 3:
            print(separator)
        elif (i % 2) == 0:
            print(between_sep)
        else:
            row = [" " if x == '' else x for x in field[0]]
            print(values.format(row[0], row[1], row[2]))
            field.pop(0)


def get_turn(board: Board, *argv) -> int:
    """Gets valid move for human player"""

    print("Where do you want to set your mark?:")
    print("Please enter a number from 1 to 9")

    valid_move = False
    pos = 0
    while not valid_move:
        pos = get_number()
        if pos == 0:
            exit(0)
        pos -= 1
        valid_move = board.check_valid_move(pos)
        if not valid_move:
            print("Move not possible.")

    return pos

