import copy
import random

from board import Board


def get_comp_turn(board: Board, comp_char: str) -> int:
    """Gets the move for the computer player"""
    print("Calculating...")
    # Randomize the move if it is the first turn, otherwise the computer will make the same move
    return int(random.uniform(0, 9)) if first_turn(board) else minmax(board, comp_char, -1)[1]


def first_turn(board: Board) -> bool:
    """Checks if it is the first turn of the game"""
    return not list(filter(lambda row: len(set(row)) != 1, board.field))


def minmax(board: Board, player_char: str, move: int, depth=0) -> (int, int):
    """Calculates the best move for the computer to make, for a given board"""
    # Base Case if the Board is finished
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
        # No need to get best move out of this call, since we already have it in the index
        move_score = -minmax(new_board, opponent, i, depth + 1)[0]

        if move_score >= score:
            score = move_score
            move = i

    return score, move
