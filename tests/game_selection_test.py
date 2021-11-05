import pytest
import mock
from mock import patch
from mock import Mock

from ..lib.ui import UI
from ..lib.game_selection import *
from ..lib.tictactoe_board import *


class TestGameSelections:
    def test_display_method_was_called_with_welcome_message(
        self, game_selection_object
    ):
        with patch.object(UI, "display", autospect=True) as mock_display:
            game_selection_object.display_welcome_message()
        mock_display.assert_called_with("Welcome to TIC TAC TOE!")

    @patch.object(UI, "get_user_input", side_effect=["g", "c", "h", "c"])
    def test_display_method_was_called_with_invalid_input_message(
        self, mock_input, game_selection_object
    ):
        with patch.object(UI, "display", autospect=True) as mock_display:
            game_selection_object.select_game_type()
        mock_display.assert_any_call("Invalid choice, try again!")

    @patch.object(UI, "get_user_input", side_effect=["h", "g", "f"])
    def test_select_game_type_returns_two_human_players(
        self, mock_input, game_selection_object
    ):
        players = game_selection_object.select_game_type()
        assert (
            isinstance(players[0], HumanPlayer) == True
            and isinstance(players[0], HumanPlayer) == True
        )

    @patch.object(UI, "get_user_input", side_effect=["c", "g", "j"])
    def test_select_game_type_returns_a_human_player_and_a_computer_players(
        self, mock_input, game_selection_object
    ):
        players = game_selection_object.select_game_type()
        assert (
            isinstance(players[1], HumanPlayer) == True
            and isinstance(players[0], ComputerPlayer) == True
        )

    @patch.object(UI, "get_user_input", side_effect=["$"])
    def test_select_a_marker(self, mock_input, game_selection_object):
        assert game_selection_object.select_a_marker("player") == "$"

    @patch.object(UI, "get_user_input", side_effect=["$$", "*"])
    def test_select_a_marker_invalid_if_2_symbols(
        self, mock_input, game_selection_object
    ):
        with patch.object(UI, "display", autospect=True) as mock_display:
            game_selection_object.select_a_marker("player")
        mock_display.assert_any_call(
            "The marker must be a single character. Try again!"
        )

    @patch.object(UI, "get_user_input", side_effect=[" ", "@"])
    def test_select_a_marker_invalid_if_choose_empty_space(
        self, mock_input, game_selection_object
    ):
        with patch.object(UI, "display", autospect=True) as mock_display:
            game_selection_object.select_a_marker("player")
        mock_display.assert_any_call(
            "The marker must be a single character. Try again!"
        )
