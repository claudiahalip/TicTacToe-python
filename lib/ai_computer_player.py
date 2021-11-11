from .tictactoe_board import *
import time
import math


class AiComputerPlayer:
    def __init__(self, board, mark, ui):
        self.board = board
        self.mark = mark
        self.ui = ui

    def move(self):
        self.ui.display("The computer is thinking.....")
        time.sleep(1)
        index = self.ai_index()
        self.board.mark_position(index, self.mark)
        self.board.display_board()

    def get_winner(self, player):
        for win_comb in self.board.win_combinations():
            win = {}
            for num in win_comb:
                win.update({num: self.board.board[num]})
            if all(value == player for value in win.values()):
                return player

    def is_a_winner(self, player):
        for win_comb in self.board.win_combinations():
            win = {}
            for num in win_comb:
                win.update({num: self.board.board[num]})
            if all(value == player for value in win.values()):
                return True
            else:
                return False

    def minimax(self, depth, is_max, player_1, player_2):
        if (
            self.board.is_board_full()
            and not self.is_a_winner(player_1)
            and not self.is_a_winner(player_2)
        ):
            return 0
        elif self.get_winner(player_1):
            return 10 - depth

        elif self.get_winner(player_2):
            return -10 + depth

        if is_max:
            current_player = player_1
        else:
            current_player = player_2

        best_score = None
        for position in self.board.get_empty_spaces():
            self.board.mark_position(position, current_player)
            score = self.minimax(depth + 1, not is_max, player_1, player_2)
            self.board.mark_position(position, self.board.empty_space)
            if best_score == None:
                best_score = score
            elif is_max:
                best_score = max(best_score, score)
            else:
                best_score = min(best_score, score)

        return best_score

    def ai_index(self):
        best_score = -math.inf
        best_move = None
        for position in self.board.get_empty_spaces():
            self.board.mark_position(position, self.mark)
            score = self.minimax(0, False, self.mark, "O")
            self.board.mark_position(position, self.board.empty_space)
            if score > best_score:
                best_score = score
                best_move = position
        return best_move
