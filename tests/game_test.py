from ..lib.game import Game
from ..lib.game import *
from ..lib.board import *
from ..lib.ui import *
import pytest
import mock
from mock import patch
from mock import Mock


class TestPlayGame:
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

    # test turn method
    @mock.patch("builtins.input")
    def test_the_input_is_valid_and_the_position_is_taken(self, mock_input):
        mock_input.return_value = "1"
        ui = Mock()
        board = Board(ui)
        game = Game(board, ui)
        # game.take_turns("X")

    def test_valid_input(self):
        ui = UI()
        new_board = Board(ui)
        game = Game(new_board, ui)
        assert game.valid_input("1") == True
        assert game.valid_input("0") == False

    def test_switch_players_for_next_player_method(self):
        ui = UI()
        board = Board(ui)
        game = Game(board, ui)
        game.switch_players()
        assert game.current_player == "O"
