class HumanPlayer:
    def __init__(self, ui, board, mark):
        self.ui = ui
        self.board = board
        self.mark = mark

    def move(self):
        self.ui.display("Choose an open space between 1 and 9:")
        input_number = self.ui.get_user_input()
        if self.board.valid_input(input_number) and not self.board.is_position_taken(
            input_number
        ):
            self.board.mark_position(input_number, self.mark)
            self.board.display_board()
        else:
            self.ui.display("Invalid number")
            self.move()
