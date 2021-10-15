class Board:

    cell = " "

    def __init__(self):
        self.board = {
            "1": self.cell,
            "2": self.cell,
            "3": self.cell,
            "4": self.cell,
            "5": self.cell,
            "6": self.cell,
            "7": self.cell,
            "8": self.cell,
            "9": self.cell,
        }

    def display_board(self):
        print(self.board["1"] + " | " + self.board["2"] + " | " + self.board["3"])
        print("-----------")
        print(self.board["4"] + " | " + self.board["5"] + " | " + self.board["6"])
        print("-----------")
        print(self.board["7"] + " | " + self.board["8"] + " | " + self.board["9"])

    def move(self, input, mark):
        self.board[input] = mark

    def position_taken(self, input):
        return self.board[input] != self.cell

    def board_full(self):
        return self.cell not in self.board.values()
