from .board import *


class ComputerPlayer:
    def __init__(self, ui, board, mark):
        self.ui = ui
        self.board = board
        self.mark = mark

    def mark_position(self):
        input_number = self.computer_input()
        self.board.move(input_number, self.mark)
        self.board.display_board()

    def computer_input(self):
        values = list(self.board.board.values())
        input = values.index(" ")
        return input + 1
