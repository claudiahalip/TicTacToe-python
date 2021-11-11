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

    def is_board_full(self):
        return self.empty_space not in self.board.values()

    def is_input_valid(self, input):
        return int(input) in self.board.keys()

    def get_empty_spaces(self):
        return [k for k in self.board if self.board[k] == self.empty_space]
