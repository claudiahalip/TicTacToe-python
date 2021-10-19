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
        current_player = "X"
        while not self.board.board_full(self.board.board):
            self.turn(current_player)
            current_player = self.next_player(current_player)

    def turn(self, mark):
        self.ui.display("Choose a number between 1 and 9:")
        input_number = input()

        if self.valid_input(input_number) and not self.board.position_taken(
            input_number
        ):
            self.board.move(input_number, mark)
            self.board.display_board()
            self.ui.display("It's " + self.next_player(mark) + "'s turn")
        else:
            self.ui.display("Invalid number")
            self.turn(mark)

    def valid_input(self, input):
        return input in self.board.board.keys()

    def next_player(self, mark):
        if mark == "X":
            return "O"
        elif mark == "O":
            return "X"
