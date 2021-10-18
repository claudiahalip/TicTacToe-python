from .board import *
from .ui import *


class PlayGame:
    def __init__(self, board, ui):
        self.board = board
        self.ui = ui

    def start(self):
        self.ui.display("Welcome to TIC TAC TOE!")
        self.board.display_board()
        self.ui.display("X goes first")
        while not self.board.board_full(self.board.board):
            self.turn()

    def turn(self):
        self.ui.display("Choose a number between 1 and 9:")
        input_number = input()
        if self.valid_input(input_number) and not self.board.position_taken(
            input_number
        ):
            mark = self.current_mark()
            self.board.move(input_number, mark)
            self.board.display_board()
            self.display_player_turn(mark)
        else:
            self.ui.display("Invalid number")
            self.turn()

    def valid_input(self, input):
        return input in self.board.board.keys()

    def taken_turns_count(self, dict):
        return sum(turn != " " for turn in dict.values())

    def current_mark(self):
        turns = self.taken_turns_count(self.board.board)
        if turns % 2 == 0:
            return "X"
        else:
            return "O"

    def display_player_turn(self, mark):
        if mark == "O":
            return self.ui.display("It's X's turn")
        else:
            return self.ui.display("It's O's turn")
