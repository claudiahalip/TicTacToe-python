from .tictactoe_board import *
from .computer_player import *
from .human_player import *


class GameSelection:
    def __init__(self, ui, board):
        self.ui = ui
        self.board = board

    def select_game_type(self):
        self.ui.display("Welcome to TIC TAC TOE!")
        self.ui.display("Choose h for human vs. human game or c for human vs computer")
        input = self.ui.get_user_input()
        if input == "h":
            current_player = HumanPlayer(self.ui, self.board, "X")
            next_player = HumanPlayer(self.ui, self.board, "O")
            return [current_player, next_player]
        elif input == "c":
            current_player = HumanPlayer(self.ui, self.board, "X")
            next_player = ComputerPlayer(self.board, "O")
            return [current_player, next_player]
        else:
            self.ui.display("Invalid choice, try again!")
            self.select_game_type()
