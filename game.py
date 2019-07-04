#! /usr/bin/env python3
import copy
import random
import time
from os import system

from board import Board


class Game():
    player_turn = False
    other_char = 'O'
    player_char = 'X'

    def __init__(self):
        self.greeting()
        self.get_other_player_turn = self.get_player_turn if self.single_player else self.get_ai_turn


    def start_game(self):
        """
        Main method to call, to start the game
        """
        continue_game = True
        self.over = False
        while continue_game:
            self.player_turn = int(random.uniform(0, 2)) # Decides who starts
            self.board = Board()
            self.first_turn = True
            self.run()
            self.over = False                        # Resets the 'over' state if player wants to play again
            continue_game = self.play_again()
            system('clear')


    def run(self):
        """
        Runs one instance of a Tic-tac-toe game, until a player wins or the game ends in a draw 
        """
        self.board.draw_field([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])
        while not self.over:
            pos = self.get_player_turn() if self.player_turn else self.get_other_player_turn()
            char = self.player_char if self.player_turn else self.other_char
            self.board.update_board(pos, char)
            self.over = self.board.game_finished()
            system('clear')
            self.player_turn = not self.player_turn
            self.board.draw_field()
        self.print_winner(self.over)


    def play_again(self):
        again = ''
        while again != 'yes' and again != 'no':
            print("Do you want to play again?[yes/no]")
            again = input().strip().lower()
        return True if again == 'yes' else False


    def get_player_turn(self):
        if self.first_turn:
            self.first_turn = False

        print("Where do you want to set your mark?:")
        print("Enter from 1 to 9")
        valid_move = False

        while not valid_move:
            pos = self.get_user_input_number()
            pos -= 1
            valid_move = self.board.check_valid_move(pos)
            if not valid_move:
                print("Move not possible.")

        return pos


    def get_ai_turn(self):
        print("Calculating...")

        if self.first_turn:                     #If computer draws first, make it random, otherwise it's the same move
            self.first_turn = False
            return int(random.uniform(0, 9))

        move = minmax(self.board, self.other_char, -1)[1]
        return move


    def get_user_input_number(self):
        try:
            return int(input())
        except:
            print("Input could not be read. Please enter a number.")
            return False


    def greeting(self):
         
        def right_number(number):
            return number == 1 or number == 2

        strings = ["Welcome", "To a game of Tic-Tac-toe", "First things first."]
        for string in strings:
            print(string)
            time.sleep(1)
        print("Do you want play as two, or alone against the frustrating AI? (Enter '1' or '2' for number of players): ")

        number = 0
        while not right_number(number):
            number = self.get_user_input_number()
            if not right_number(number):
                print("Please enter '1' to against the Computer or '2' if you play with a friend.")

        self.single_player = number - 1
            
    def print_winner(self, winner):

        if winner == True:
            print("*******************************************")
            print("The game ended in a draw.")
            print("*******************************************")
            return
        print("*******************************************")
        print('\'' + winner + "\' won.")
        print("*******************************************")


def minmax(board, player_char, move, depth=0):
    # Base Case if board is finished
    player_won = board.game_finished()
    if player_won:
        score = 10 - depth if (player_won == player_char) else depth - 10
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

        opponent = 'O' if (player_char == 'X') else 'X'          # Switches char for minmax call

        move_score = -minmax(new_board, opponent, i, depth + 1)[0]      # No need to get best move out of this call, since we already have it in 'i'

        if move_score > score:
            score = move_score
            move = i

    return score, move


Game().start_game()
