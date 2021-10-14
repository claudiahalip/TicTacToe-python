class Board:
    def __init__(self):
        self.board = {
            "1": " ",
            "2": " ",
            "3": " ",
            "4": " ",
            "5": " ",
            "6": " ",
            "7": " ",
            "8": " ",
            "9": " ",
        }

    def display_board(self):
        print(self.board["1"] + "  | " + self.board["2"] + " | " + self.board["3"])
        print("-----------")
        print(self.board["4"] + "  | " + self.board["5"] + " | " + self.board["6"])
        print("-----------")
        print(self.board["7"] + "  | " + self.board["8"] + " | " + self.board["9"])

    def move(self, input, mark):
        self.board[input] = mark

    def position_taken(self, input):
        return self.board[input] != " "

    def board_full(self):
        return " " not in self.board.values()
