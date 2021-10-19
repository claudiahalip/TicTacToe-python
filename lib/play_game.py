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
            mark = self.current_mark(input_number)
            self.board.move(input_number, mark)
            self.board.display_board()
            next_player = int(input_number) + 1
            self.ui.display("It's " + self.current_mark(next_player) + "'s turn")
        else:
            self.ui.display("Invalid number")
            self.turn()

    def valid_input(self, input):
        return input in self.board.board.keys()

    def current_mark(self, input):
        if int(input) % 2 == 0:
            return "O"
        else:
            return "X"
