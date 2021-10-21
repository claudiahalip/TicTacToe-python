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
    # TRUE, TRUE
    @patch.object(Board, "move")
    @patch.object(Board, "display_board")
    def test_the_take_turns_method_when_the_input_is_valid_and_the_position_is_not_taken_1(
        self, mock_move, mock_display_board
    ):
        ui = Mock()
        board = Board(ui)
        game = Game(board, ui)
        game.take_turns("X", "1")
        mock_move.assert_called()
        mock_display_board.assert_called()

    # TRUE, FALSE
    @patch.object(UI, "display")
    def test_the_take_turns_method_when_the_input_is_valid_and_the_position_is_taken(
        self, mock_display
    ):
        ui = Mock()
        board = Board(ui)
        board.move("5", "X")
        game = Game(board, ui)
        game.take_turns("X", "5")
        mock_display.assert_called

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
