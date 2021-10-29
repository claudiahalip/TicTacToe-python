import pytest
import mock
from mock import patch
from mock import Mock

from ..lib.human_player import HumanPlayer
from ..lib.game import *
from ..lib.ui import *
from ..lib.tictactoe_board import *


class TestsHumanPlayer:

    # #tests for mark_position method
    # True, true
    @patch.object(UI, "get_user_input", side_effect=["2", "3"])
    @patch.object(Board, "mark_position")
    def test_move_when_the_input_is_valid_and_the_position_is_not_taken(
        self, mock_input, mock_mark_position, player_object
    ):
        player_object.move()
        mock_mark_position.assert_called_once()

    # # True, false
    @patch.object(UI, "get_user_input", side_effect=["4", "2"])
    @patch.object(UI, "display")
    def test_the_move_when_the_input_is_valid_and_the_position_is_taken(
        self, mock_display, mock_input, player_object
    ):
        player_object.move()
        mock_display.assert_any_call("Invalid number")

    # False, true
    @patch.object(UI, "get_user_input", side_effect=["0", "2"])
    @patch.object(UI, "display")
    def test_the_mark_position_when_the_input_is_not_valid_and_the_position_is_not_taken(
        self, mock_display, mock_input, player_object
    ):
        player_object.move()
        mock_display.assert_any_call("Invalid number")

    # false, false
    @patch.object(UI, "get_user_input", side_effect=["0", "3", "2"])
    @patch.object(UI, "display")
    def test_the_mark_position_when_the_input_is_not_valid_and_the_position_is_taken(
        self, mock_display, mock_input, player_object
    ):
        player_object.move()
        mock_display.assert_any_call("Invalid number")
