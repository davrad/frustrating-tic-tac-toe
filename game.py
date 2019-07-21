#! /usr/bin/env python3
import copy
import random
import time
from os import system

from board import Board


class Game:
    other_char = 'O'
    player_char = 'X'

    def __init__(self):
        """Starts Tic-tac-toe games until until the player wants to quit"""
        single_player = greeting()
        self.get_other_player_turn = self.get_player_turn if single_player else self.get_ai_turn
        while True:
            # Random start
            self.player_turn = int(random.uniform(0, 2))
            self.board = Board()
            self.first_turn = True
            self.play_game()
            if not play_again():
                break
            system('clear')

    def play_game(self):
        """Starts one instance of Tic-tac-toe"""
        self.board.draw_field([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])
        while True:
            pos = self.get_player_turn() if self.player_turn else self.get_other_player_turn()
            char = self.player_char if self.player_turn else self.other_char
            self.update_board(pos, char)
            system('clear')
            self.player_turn = not self.player_turn
            self.board.draw_field()
            if self.finished():
                winner = self.get_winner()
                break
        print_winner(winner)

    def update_board(self, pos, char):
        self.board.update_board(pos, char)

    def get_winner(self) -> str:
        return self.board.get_winner()

    def finished(self) -> bool:
        return self.board.game_finished()

    def get_player_turn(self) -> int:
        """Gets valid move for human player"""
        if self.first_turn:
            self.first_turn = False

        print("Where do you want to set your mark?:")
        print("Please enter a number from 1 to 9")

        valid_move = False
        pos = 0
        while not valid_move:
            pos = get_user_input_number()
            if pos == 0:
                exit(0)
            pos -= 1
            valid_move = self.board.check_valid_move(pos)
            if not valid_move:
                print("Move not possible.")

        return pos

    def get_ai_turn(self) -> int:
        """Gets the move for the computer player"""
        print("Calculating...")
        # If computer draws first, make it random, otherwise same move
        if self.first_turn:
            self.first_turn = False
            return int(random.uniform(0, 9))

        move = minmax(self.board, self.other_char, -1)[1]
        return move


def greeting() -> int:
    """Gets the player decision whether to play alone or together"""

    def right_number(n):
        return n == 1 or n == 2

    strings = ["Welcome", "To a game of Tic-Tac-toe", "First things first."]
    for s in strings:
        print(s)
        time.sleep(1)
    print(
        "Do you want play as two, or alone against the frustrating AI? (Enter '1' or '2' for number of players): ")

    number = 0
    while not right_number(number):
        number = get_user_input_number()
        if not right_number(number):
            print("Please enter '1' to play against the Computer or '2' if you play with a friend.")
    print("If you want to quit please enter '0', when prompted to check a field.")
    return number - 1


def play_again() -> bool:
    """Asks if the player wants to play again"""
    again = ''
    while again != 'yes' and again != 'no':
        print("Do you want to play again?[yes/no]")
        again = input().strip().lower()
    return True if again == 'yes' else False


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


def get_user_input_number() -> int:
    """Gets user input number"""
    while True:
        try:
            return int(input())
        except ValueError:
            print("Input could not be read. Please enter a number.")


def minmax(board: Board, player_char: str, move: int, depth=0) -> (int, int):
    """Calculates the best move for the computer to make"""
    # Base Case if Board is finished
    if board.game_finished():
        player_won = board.get_winner()
        score = 10 - depth if (player_won == player_char) else depth - 10
        if player_won == '':
            score = 0
        return score, move
    # Values to represent they're invalid
    move = -100
    score = -100
    # Try out every possible move and call minmax recursively
    for i in range(9):
        if board.field[i // 3][i % 3] != '':
            continue

        new_board = Board(copy.deepcopy(board.field))
        new_board.field[i // 3][i % 3] = player_char
        # Switches char for minmax call
        opponent = 'O' if (player_char == 'X') else 'X'
        # No need to get best move out of this call, since we already have it in 'i'
        move_score = -minmax(new_board, opponent, i, depth + 1)[0]

        if move_score >= score:
            score = move_score
            move = i

    return score, move


Game()
