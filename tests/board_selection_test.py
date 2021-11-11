import pytest
import mock
from mock import patch
from mock import Mock

from lib.board_selection import BoardSelection
from lib.ui import UI
from lib.game_selection import *
from lib.tictactoe_board import *


class TestBoardSelection:
    @patch.object(UI, "get_user_input", side_effect=["2", "3"])
    def test_display_method_was_called_with_welcome_message(self, mock_user_input):
        ui = UI()
        board_selection = BoardSelection(ui)
        with patch.object(UI, "display", autospect=True) as mock_display:
            board_selection.select_board_size()
        mock_display.assert_any_call("Welcome to TIC TAC TOE!")

    @patch.object(UI, "get_user_input", side_effect=["3", "4"])
    def test_display_method_was_called_with_board_selection_size(self, mock_user_input):
        ui = UI()
        board_selection = BoardSelection(ui)
        with patch.object(UI, "display", autospect=True) as mock_display:
            board_selection.select_board_size()
        mock_display.assert_any_call("First, select a board size.")

    @patch.object(UI, "get_user_input", side_effect=["2", "4"])
    def test_display_method_was_called_with_invalid_board_size_message(
        self, mock_user_input
    ):
        ui = UI()
        board_selection = BoardSelection(ui)
        with patch.object(UI, "display", autospect=True) as mock_display:
            board_selection.select_board_size()
        mock_display.assert_any_call(
            "The size of the board should be one of the following: 3, 4. Try again!"
        )

    @patch.object(UI, "get_user_input", side_effect=["3"])
    def test_select_board_size_return_3x3_board_object(self, mock_user_input):
        ui = UI()
        board_selection = BoardSelection(ui)
        new_board = board_selection.select_board_size()
        assert new_board.size == 3

    @patch.object(UI, "get_user_input", side_effect=["4"])
    def test_select_board_size_return_4X4_board_object(self, mock_user_input):
        ui = UI()
        board_selection = BoardSelection(ui)
        new_board = board_selection.select_board_size()
        assert new_board.size == 4
