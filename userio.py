import time
from os import system

from board import Board


def print_winner(winner: str) -> None:
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
        word = input("Do you want to play again?[yes/no]\n")
        again = '' if len(word) == 0 else word.strip().lower()[0]
    return again == 'y'


def greeting() -> None:
    """Greets the players"""
    strings = [
        "Welcome", 
        "To a game of Tic-Tac-toe", 
        "First things first.",
        "Do you want play together, or alone against the frustrating AI? (Enter '1' or '2' for number of players): "]

    for s in strings:
        print(s)
        time.sleep(1)


def get_gamemode() -> int:
    """Gets the player decision whether to play alone or together"""
    greeting()
    number = get_number()
    while number != 1 and number != 2:
        print("Please enter '1' to play against the Computer or '2' if you play with a friend.")
        number = get_number()

    return number - 1


def draw_field(field: list) -> None:
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

    pos = get_number() - 1
    valid_move = board.check_valid_move(pos) 
    while not valid_move:
        print("Move not possible.")
        pos = get_number() - 1
        valid_move = board.check_valid_move(pos)

    return pos

