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
            self.ui.display("Game over! " + self.winner() + " is the winner.")
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
        for win_comb in self.board.win_combinations:
            if self.is_win_condition_met(win_comb):
                return True
        return False

    def is_win_condition_met(self, win_comb):
        return self.board.board[win_comb[0]] == self.board.board[
            win_comb[1]
        ] == self.board.board[win_comb[2]] and self.board.is_position_taken(win_comb[0])

    def winner(self):
        for win_comb in self.board.win_combinations:
            if self.board.board[win_comb[0]] == self.board.board[
                win_comb[1]
            ] == self.board.board[win_comb[2]] and self.board.is_position_taken(
                str(win_comb[0])
            ):
                return self.board.board[win_comb[0]]
