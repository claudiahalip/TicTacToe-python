from ..lib.board import *


class TestBoard:
    def test_move(self):
        #     move method changes the value of the given key( number from the user) from empty to the given mark
        new_board = Board()
        new_board.move(1, "X")
        assert new_board.board[1] == "X"

    def test_position_taken(self):
        # position_taken method will check if the value of the given key is not
        # not emply and return True
        new_board = Board()
        new_board.move(1, "X")
        assert new_board.position_taken(1) == True
        new_board = Board()
        new_board.move(1, " ")
        assert new_board.position_taken(1) == False

    def test_board_full(self):
        new_board = Board()
        assert new_board.board_full() == False
        new_board = Board()
        new_board.board = {"1": "O","2": "X","3": "O","4": "X","5": "O","6": "X","7": "X","8": "O","9": "X",}
        assert new_board.board_full() == True
