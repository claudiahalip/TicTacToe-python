from .ui import *
import numpy as np


class Board:

    empty_space = " "

    def __init__(self, ui, size=3):
        self.ui = ui
        self.size = size
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

    def board_rows(self):
        arr = np.array([*self.board.keys()])
        arr_with_rows = arr.reshape(self.size, self.size)
        return arr_with_rows

    def board_columns(self):
        return self.board_rows().transpose()

    def board_diagonals(self):
        first_column = []
        second_column = []
        for i in range(self.size):
            first_column.append(self.board_rows()[i][i])
            second_column.append(self.board_rows()[(i)][(self.size - 1 - i)])
        return [first_column, second_column]

    def win_combinations(self):
        win_combinbations = []
        for row_comb in self.board_rows():
            win_combinbations.append(row_comb)
        for column_comb in self.board_columns():
            win_combinbations.append(column_comb)
        for diagonal_comb in self.board_diagonals():
            win_combinbations.append(diagonal_comb)
        return win_combinbations
