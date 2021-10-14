from .board import *
from .ui import *


class PlayGame:
    def __init__(self, board, ui):
        self.board = board
        self.ui = ui

    def start(self):
        self.ui.display("Welcome to TIC TAC TOE!")
        self.board.display_board()
        while not self.board.board_full():
            self.turn()

    def turn(self):
        self.ui.display("Choose a number between 1 and 9:")
        input_number = input()
        if self.valid_input(input_number) and not self.board.position_taken(
            input_number
        ):
            self.board.move(input_number, "X")
            self.board.display_board()
        else:
            self.ui.display("Invalid number")
            self.turn()

    def valid_input(self, input):
        return input in self.board.board.keys()
