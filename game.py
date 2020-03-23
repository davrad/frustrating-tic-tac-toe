#! /usr/bin/env python3
import random

import comp_choice
import userio
from board import Board


class Game:
    other_char = 'O'
    player_char = 'X'

    def __init__(self) -> None:
        """Starts Tic-tac-toe games until the player wants to quit"""
        single_player = userio.get_gamemode()
        self.get_other_turn = userio.get_turn if single_player else comp_choice.get_comp_turn
        playing = True
        while playing:
            # Random start
            self.player_turn = int(random.uniform(0, 2))
            self.board = Board()
            self.play_game()
            playing = userio.play_again()

    def play_game(self) -> None:
        """Starts one instance of a Tic-tac-toe game"""
        userio.draw_field([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])
        while not self.finished():
            pos = self.get_pos()
            char = self.player_char if self.player_turn else self.other_char
            self.update_board(pos, char)
            self.player_turn = not self.player_turn
            userio.draw_field(self.board.field)
        userio.print_winner(self.get_winning_char())

    def get_pos(self) -> int:
        """Gets position for current turn"""
        return userio.get_turn(self.board) if self.player_turn else self.get_other_turn(self.board, self.other_char)

    def update_board(self, pos: int, char: str) -> None:
        """Updates Field given a position on the board and a character"""
        self.board.update_board(pos, char)

    def get_winning_char(self) -> str:
        """Gets the character who won"""
        return self.board.get_winner()

    def finished(self) -> bool:
        """Checks if the board is finished"""
        return self.board.game_finished()


Game()
