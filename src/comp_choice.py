import copy
import random
from typing import Final

from board import Board

PLAYER_CHAR: Final[str] = 'X'
COMPUTER_CHAR: Final[str] = 'O'


def get_comp_turn(board: Board) -> int:
    """Gets the move for the computer player, a random one if its the first turn"""
    print("Calculating...")
    if first_turn(board):
        return int(random.uniform(0, 9))
    else:
        return minmax(board, COMPUTER_CHAR, -1)[1]


def first_turn(board: Board) -> bool:
    """Checks if it is the first turn of the game"""
    return not list(filter(lambda row: len(set(row)) != 1, board.field))


def base_case(board: Board, player_char: str, depth: int) -> (int, int):
    """Base case for minmax algorithm if board is full"""
    char_won = board.get_winner()
    if char_won == '':
        return 0
    return 10 - depth if (char_won == player_char) else depth - 10


def possible_cells(board: Board) -> list:
    """Returns a list of indices where cell on the field is empty"""
    return list(filter(lambda i: board.field[i // 3][i % 3] == '', range(9)))


def recursive_call(board: Board, player_char: str, i: int, depth: int, move: int, score: int) -> (int, int):
    """Calls minmax recursively and returns the better score and move"""
    new_board = Board(copy.deepcopy(board.field))
    new_board.field[i // 3][i % 3] = player_char
    opponent = 'O' if (player_char == 'X') else 'X'
    move_score = -minmax(new_board, opponent, i, depth + 1)[0]
    if move_score >= score:
        score = move_score
        move = i
    return score, move


def minmax(board: Board, player_char: str, move: int, depth=0) -> (int, int):
    """Calculates the best move for the computer to make, for a given board"""
    if board.game_finished():
        return base_case(board, player_char, depth), move
    move = score = -100
    for i in possible_cells(board):
        score, move = recursive_call(board, player_char, i, depth, move, score)
    return score, move
