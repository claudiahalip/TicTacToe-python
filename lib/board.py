class Board:
    def __init__(self):
        self.board = {
            "1": None,
            "2": None,
            "3": None,
            "4": None,
            "5": None,
            "6": None,
            "7": None,
            "8": None,
            "9": None,
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
        return self.board[input] != " "

    def board_full(self):
        return None not in self.board.values()
