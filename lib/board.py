class Board:

    empty_space = " "

    def __init__(self):
        self.board = {
            "1": self.empty_space,
            "2": self.empty_space,
            "3": self.empty_space,
            "4": self.empty_space,
            "5": self.empty_space,
            "6": self.empty_space,
            "7": self.empty_space,
            "8": self.empty_space,
            "9": self.empty_space,
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
        return self.board[input] != self.empty_space

    def board_full(self, dict):
        return self.empty_space not in dict.values()
