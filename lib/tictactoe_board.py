from .board import *
from .ui import *


class TicTacToeBoard(Board):
    def display_board(self):
        for key in self.board:
            if int(key) % self.size == 0 and int(key) != self.size ** 2:
                self.ui.display(self.board[key] + "\n" + "-" * self.size * 2)
            elif int(key) == self.size ** 2:
                self.ui.display(self.board[key] + "\n")
            else:
                print(self.board[key], end="|")
