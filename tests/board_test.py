import pytest
from ..lib.board import *
from ..lib.game import *
from ..lib.board import *
from ..lib.ui import *
import pytest
import mock
from mock import patch
from mock import Mock


class TestBoard:
    def test_move_marks_the_board_with_marker(self):
        ui = UI()
        new_board = Board(ui)
        new_board.move(1, "X")
        assert new_board.board[1] == "X"

    # test for position_taken method
    @pytest.mark.parametrize("test_input, expected", [("1", False), ("2", True)])
    def test_position_taken(self, test_input, expected):
        ui = UI()
        new_board = Board(ui)
        new_board.move("2", "X")
        assert new_board.position_taken(test_input) == expected

    @pytest.mark.parametrize(
        "test_input, expected",
        [
            (
                {
                    "1": "O",
                    "2": "X",
                    "3": "O",
                    "4": "X",
                    "5": "O",
                    "6": "X",
                    "7": "X",
                    "8": "O",
                    "9": "X",
                },
                True,
            ),
            (
                {
                    "1": " ",
                    "2": " ",
                    "3": " ",
                    "4": " ",
                    "5": " ",
                    "6": " ",
                    "7": " ",
                    "8": " ",
                    "9": " ",
                },
                False,
            ),
        ],
    )
    def test_board_full(self, test_input, expected):
        ui = UI()
        board = Board(ui)
        assert board.board_full(test_input) == expected
