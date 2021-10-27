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
    def test_move_marks_the_board_with_marker(self, board_object):
        board_object.move(1, "X")
        assert board_object.board[1] == "X"

    # test for position_taken method
    @pytest.mark.parametrize("test_input, expected", [(1, False), (2, True)])
    def test_position_taken(self, test_input, expected, board_object):
        board_object.move(2, "X")
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
        assert board_object.board_is_full() == True

    def test_board_is_not_full_(self, board_object):
        assert board_object.board_is_full() == False
