from .tictactoe_board import *
import time
import math


class ComputerPlayer:
    def __init__(self, board, mark, ui):
        self.board = board
        self.mark = mark
        self.ui = ui

    def move(self):
        self.ui.display("The computer is thinking.....")
        time.sleep(1)
        index = self.next_available_space_index()
        self.board.mark_position(index, self.mark)
        self.board.display_board()

    def next_available_space_index(self):
        values = list(self.board.board.values())
        input = values.index(self.board.empty_space)
        return input + 1
