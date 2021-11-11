from .ui import *
from .tictactoe_board import *


class Game:
    def __init__(self, board, ui, players):
        self.board = board
        self.ui = ui
        self.current_player = players[0]
        self.next_player = players[1]

    def start(self):
        self.board.display_board()
        self.ui.display(self.current_player.mark + " goes first")
        while not self.is_over():
            self.take_turns()
            self.switch_players()
        if self.is_a_win():
            self.ui.display("Game over! " + self.get_winner() + " is the winner.")
        else:
            self.ui.display("Game over! It's a draw.")

    def take_turns(self):
        self.current_player.move()
        if not self.is_over():
            self.ui.display("It's " + self.next_player.mark + "'s turn")

    def switch_players(self):
        self.current_player, self.next_player = self.next_player, self.current_player

    def is_over(self):
        return self.board.is_board_full() or self.is_a_win()

    def is_a_win(self):
        if self.is_a_winner(self.current_player.mark) or self.is_a_winner(
            self.next_player.mark
        ):
            return True
        return False

    def get_winner(self):
        if self.is_a_winner(self.current_player.mark):
            return self.current_player.mark
        else:
            return self.next_player.mark

    def is_a_winner(self, player):
        for win_comb in self.board.win_combinations():
            win = {}
            for num in win_comb:
                win.update({num: self.board.board[num]})
            if all(value == player for value in win.values()):
                return True
        else:
            return False
