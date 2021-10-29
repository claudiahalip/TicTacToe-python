from .ui import *


class Board:

    empty_space = " "

    def __init__(self, ui, size=3):
        self.ui = ui
        self.board = dict.fromkeys(range(1, (size ** 2) + 1), self.empty_space)

    def mark_position(self, input, mark):
        self.board[int(input)] = mark

    def is_position_taken(self, input):
        return self.board[int(input)] != self.empty_space

    def board_is_full(self):
        return self.empty_space not in self.board.values()

    def valid_input(self, input):
        return int(input) in self.board.keys()
