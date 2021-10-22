from .ui import *


class Board:

    empty_space = " "

    def __init__(self, ui):
        self.ui = ui
        self.board = {
            "1": self.empty_space,
            "2": self.empty_space,
            "3": self.empty_space,
            "4": self.empty_space,
            "5": self.empty_space,
            "6": self.empty_space,
            "7": self.empty_space,
            "8": self.empty_space,
            "9": self.empty_space,
        }
        self.win_combinations = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9],
            [1, 5, 9],
            [3, 5, 7],
        ]

    def display_board(self):
        for key in self.board:
            if int(key) % 3 == 0 and int(key) != 9:
                self.ui.display(self.board[key] + "\n" + "---------")
            elif int(key) == 9:
                self.ui.display(self.board[key] + "\n")
            else:
                print(self.board[key], end=" | ")

    def move(self, input, mark):
        self.board[input] = mark

    def position_taken(self, input):
        return self.board[input] != self.empty_space

    def board_is_full(self):
        return self.empty_space not in self.board.values()
