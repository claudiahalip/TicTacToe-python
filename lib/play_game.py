from .board import *
from .ui import *


class PlayGame:
    def __init__(self, board, ui):
        self.board = board
        self.ui = ui

    def start(self):
        self.ui.display("Welcome to TIC TAC TOE!")
        self.board.display_board()
