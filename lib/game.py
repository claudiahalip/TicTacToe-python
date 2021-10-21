from .board import *
from .ui import *


class Game:

    current_player = "X"
    next_player = "O"

    def __init__(self, board, ui):
        self.board = board
        self.ui = ui

    def start(self):
        self.ui.display("Welcome to TIC TAC TOE!")
        self.board.display_board()
        self.ui.display(self.current_player + " goes first")
        while not self.board.board_full(self.board.board):
            self.ui.display("Choose a number between 1 and 9:")
            input_number = self.ui.get_user_input()
            self.take_turns(self.current_player, input_number)
            self.switch_players()

    def take_turns(self, mark, input_number):
        if self.valid_input(input_number) and not self.board.position_taken(
            input_number
        ):
            self.board.move(input_number, mark)
            self.board.display_board()
            self.ui.display("It's " + self.next_player + "'s turn")
        else:
            self.ui.display("Invalid number")

    def valid_input(self, input):
        return input in self.board.board.keys()

    def switch_players(self):
        self.current_player, self.next_player = self.next_player, self.current_player
