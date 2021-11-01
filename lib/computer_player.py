from .board import *


class ComputerPlayer:
    def __init__(self, board, mark):
        self.board = board
        self.mark = mark

    def move(self):
        input_number = self.next_available_space_index()
        self.board.mark_position(input_number, self.mark)
        self.board.display_board()

    def next_available_space_index(self):
        values = list(self.board.board.values())
        input = values.index(" ")
        return input + 1
