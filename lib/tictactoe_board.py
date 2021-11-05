from .board import *
from .ui import *


class TicTacToeBoard(Board):

    win_combinations = [
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
