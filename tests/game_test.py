from ..lib.game import Game
from ..lib.game import *
from ..lib.board import *
from ..lib.ui import *
import pytest
import mock
from mock import patch
from mock import Mock


class TestGame:
    def test_display_method_was_called(self):
        board = Mock()
        ui = UI()
        with patch.object(UI, "display", autospect=True) as mock_display:
            game = Game(board, ui)
            game.start()
        mock_display.assert_called

    def test_display_board_method_was_called(self):
        board = Mock()
        ui = UI()
        with patch.object(Board, "display_board", autospect=True) as mock_display_board:
            game = Game(board, ui)
            game.start()
        mock_display_board.assert_called

    def test_take_turns_method_was_called(self):
        ui = UI()
        board = Mock()
        with patch.object(Game, "take_turns", autospec=True) as mock_take_turns:
            game = Game(board, ui)
            game.start()
            mock_take_turns.assert_called

    # #tests for take_turns method
    # True, true
    @patch.object(UI, "get_user_input", side_effect=["2", "3"])
    @patch.object(Board, "display_board")
    @patch.object(Board, "move")
    def test_the_take_turns_when_the_input_is_valid_and_the_position_is_not_taken(
        self, mock_input, mock_move, mock_display_board
    ):
        ui = UI()
        board = Board(ui)
        game = Game(board, ui)
        game.take_turns("X")
        mock_move.assert_called_once()
        mock_display_board.assert_called_once()

    # True, false
    @patch.object(UI, "get_user_input", side_effect=["3", "2"])
    @patch.object(UI, "display")
    def test_the_take_turns_when_the_input_is_valid_and_the_position_is_taken(
        self, mock_display, mock_input
    ):
        ui = UI()
        board = Board(ui)
        game = Game(board, ui)
        board.move("3", "X")
        game.take_turns("X")
        mock_display.assert_any_call("Invalid number")

    # False, true
    @patch.object(UI, "get_user_input", side_effect=["0", "2"])
    @patch.object(UI, "display")
    def test_the_take_turns_when_the_input_is_not_valid_and_the_position_is_not_taken(
        self, mock_display, mock_input
    ):
        ui = UI()
        board = Board(ui)
        game = Game(board, ui)
        game.take_turns("X")
        mock_display.assert_any_call("Invalid number")

    # false, false
    @patch.object(UI, "get_user_input", side_effect=["0", "3", "2"])
    @patch.object(UI, "display")
    def test_the_take_turns_when_the_input_is_not_valid_and_the_position_is_taken(
        self, mock_display, mock_input
    ):
        ui = UI()
        board = Board(ui)
        game = Game(board, ui)
        board.move("3", "X")
        game.take_turns("X")
        mock_display.assert_any_call("Invalid number")

    @pytest.mark.parametrize("input, expected", [("1", True), ("0", False)])
    def test_valid_input(self, input, expected):
        ui = UI()
        new_board = Board(ui)
        game = Game(new_board, ui)
        assert game.valid_input(input) == expected

    def test_switch_players_for_next_player_method(self):
        ui = UI()
        board = Board(ui)
        game = Game(board, ui)
        game.switch_players()
        assert game.current_player == "O"
