import random
from typing import Callable, Final

import comp_choice
import userio
from board import Board

GetTurnFunction = Callable[[Board], int]


class Game:
    PLAYER_CHAR: Final[str] = 'X'
    OTHER_PLAYER_CHAR: Final[str] = 'O'

    def __init__(self, *args, **kwargs) -> None:
        """Starts Tic-tac-toe games until the player wants to quit"""
        single_player: bool = userio.ask_user_play_singleplayer()
        self.get_other_turn: GetTurnFunction
        if single_player:
            self.get_other_turn = comp_choice.get_comp_turn
        else:
            self.get_other_turn = userio.get_turn
        playing: bool = True
        while playing:
            self.board = Board()
            self.play_game()
            playing = userio.play_again()

    def play_game(self) -> None:
        """Starts one instance of a Tic-tac-toe game"""
        userio.draw_field([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])
        # 50:50 chance if the first player begins
        self.player_turn = int(random.uniform(0, 2))

        while not self.finished():
            pos = self.get_pos()
            char = self.PLAYER_CHAR if self.player_turn else self.OTHER_PLAYER_CHAR
            self.update_board(pos, char)
            self.player_turn = not self.player_turn
            userio.draw_field(self.board.field)
        userio.print_winner(self.get_winning_char())

    def get_pos(self) -> int:
        """Gets position for current turn"""
        if self.player_turn:
            return userio.get_turn(self.board)
        else:
            return self.get_other_turn(self.board)

    def update_board(self, pos: int, char: str) -> None:
        """Updates Field given a position on the board and a character"""
        self.board.update_board(pos, char)

    def get_winning_char(self) -> str:
        """Gets the character who won"""
        return self.board.get_winner()

    def finished(self) -> bool:
        """Checks if the board is finished"""
        return self.board.game_finished()
