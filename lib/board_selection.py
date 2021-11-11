from .tictactoe_board import TicTacToeBoard


class BoardSelection:

    valid_board_sizes = ["3", "4"]

    def __init__(self, ui):
        self.ui = ui

    def select_board_size(self):
        self.ui.display("Welcome to TIC TAC TOE!")
        self.ui.display("First, select a board size.")
        size = self.ui.get_user_input()
        while size not in self.valid_board_sizes or not size.isnumeric():
            self.ui.display(
                "The size of the board should be one of the following: "
                + self.board_sizes_for_invalid_message()
                + ". Try again!"
            )
            size = self.ui.get_user_input()
        return TicTacToeBoard(self.ui, int(size))

    def board_sizes_for_invalid_message(self):
        sizes = ""
        for size in self.valid_board_sizes:
            sizes = sizes + str(size) + ", "
        return sizes[:-2]
