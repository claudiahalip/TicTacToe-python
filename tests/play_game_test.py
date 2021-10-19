from ..lib.play_game import *
from ..lib.board import *
from ..lib.ui import *
import pytest
import mock
from mock import patch
from mock import Mock


class TestPlayGame:
    def test_display_welcome_message(self):
        board = Mock()
        ui = UI()
        with patch.object(UI, "display", autospect=True) as mock_display:
            play_game = PlayGame(board, ui)
            play_game.start()
        mock_display.assert_called

    def test_display_board(self):
        board = Mock()
        ui = UI()
        with patch.object(Board, "display_board", autospect=True) as mock_display_board:
            play_game = PlayGame(board, ui)
            play_game.start()
        mock_display_board.assert_called

    def test_valid_input(self):
        ui = UI()
        new_board = Board(ui)
        play_game = PlayGame(new_board, ui)
        assert play_game.valid_input("1") == True
        assert play_game.valid_input("0") == False

    @pytest.mark.parametrize("input, expected", [("O", "X"), ("X", "O")])
    def test_switch_players_for_next_player_method(self, input, expected):
        board = Mock()
        ui = UI()
        play_game = PlayGame(board, ui)
        assert play_game.next_player(input) == expected
