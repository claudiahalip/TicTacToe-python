from numpy import array
import pytest
from lib.board import *
from lib.game import *
from lib.board import *
from lib.ui import *
import pytest
import mock
from mock import patch
from mock import Mock


class TestBoard:
    def test_mark_position_marks_the_board_with_marker(self, board_object):
        board_object.mark_position(1, "X")
        assert board_object.board[1] == "X"

    # test for position_taken method
    @pytest.mark.parametrize("test_input, expected", [(1, False), (2, True)])
    def test__is_position_taken(self, test_input, expected, board_object):
        board_object.mark_position(2, "X")
        assert board_object.is_position_taken(test_input) == expected

    def test_board_is_full(self, board_object):
        board_object.board = {
            "1": "X",
            "2": "X",
            "3": "X",
            "4": "O",
            "5": "O",
            "6": "X",
            "7": "O",
            "8": "O",
            "9": "X",
        }
        assert board_object.is_board_full() == True

    def test_board_is_not_full_(self, board_object):
        assert board_object.is_board_full() == False

    @pytest.mark.parametrize("input, expected", [("1", True), ("0", False)])
    def test_is_input_valid(self, input, expected, board_object):
        assert board_object.is_input_valid(input) == expected

    def test_board_rows_with_3x3_board(self):
        ui = UI()
        board = Board(ui)
        array_1 = board.board_rows()
        array_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        np.testing.assert_array_equal(array_1, array_2)

    def test_board_rows_with_4X4_board(self):
        ui = UI()
        board = Board(ui, 4)
        array_1 = board.board_rows()
        array_2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        np.testing.assert_array_equal(array_1, array_2)

    def test_board_columns_with_3X3_board(self):
        ui = UI()
        board = Board(ui)
        array_1 = board.board_columns()
        array_2 = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        np.testing.assert_array_equal(array_1, array_2)

    def test_board_columns_with_4X4_board(self):
        ui = UI()
        board = Board(ui, 4)
        array_1 = board.board_columns()
        array_2 = [[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]]
        np.testing.assert_array_equal(array_1, array_2)

    def test_board_diagonals_with_3X3_board(self, board_object):
        array_1 = board_object.board_diagonals()
        array_2 = [[1, 5, 9], [3, 5, 7]]
        np.testing.assert_array_equal(array_1, array_2)

    def test_board_columns_with_4X4_board(self, board_object_with_4X4):
        array_1 = board_object_with_4X4.board_columns()
        array_2 = [[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]]
        np.testing.assert_array_equal(array_1, array_2)

    def test_win_combinations_for3x3_board(self, board_object_with_3X3):
        win_combinations = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9],
            [1, 5, 9],
            [3, 5, 7],
        ]
        np.testing.assert_array_equal(
            board_object_with_3X3.win_combinations(), win_combinations
        )
