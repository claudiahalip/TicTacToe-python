from .ui import *
from .tictactoe_board import *
from .computer_player import *
from .human_player import *
from .ai_computer_player import *


class GameSelection:

    first_player = "First player"
    second_player = "Second player"

    def __init__(self, ui, board):
        self.ui = ui
        self.board = board

    def select_game_type(self):
        self.ui.display(
            "Select a game type: \n h for human vs. human game \n c for easy computer vs human \n a for intelligent computer vs human"
        )
        input = self.ui.get_user_input()
        if input == "h":
            return self.create_players("human")
        elif input == "c":
            return self.create_players("computer")
        elif input == "a":
            return self.create_players("ai_computer")
        else:
            self.ui.display("Invalid choice, try again!")
            return self.select_game_type()

    def select_a_marker(self, player):
        self.ui.display(player + ", you can choose a marker now!")
        marker = self.ui.get_user_input()
        while len(marker) > 1 or len(marker) == 0 or marker == " ":
            self.ui.display("The marker must be a single character. Try again!")
            marker = self.ui.get_user_input()
        return marker

    def create_players(self, player):
        marker_player_1 = self.select_a_marker(self.first_player)
        if player == "ai_computer":
            current_player = AiComputerPlayer(self.board, marker_player_1, self.ui)
        elif player == "human":
            current_player = HumanPlayer(self.ui, self.board, marker_player_1)
        elif player == "computer":
            current_player = ComputerPlayer(self.board, marker_player_1, self.ui)

        marker_player_2 = self.select_a_marker(self.second_player)
        while marker_player_1 == marker_player_2:
            self.ui.display("This marker is already used. Choose another one!")
            marker_player_2 = self.select_a_marker(self.second_player)
        next_player = HumanPlayer(self.ui, self.board, marker_player_2)
        return [current_player, next_player]
