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
        new_board = Board()
        ui = UI()
        play_game = PlayGame(new_board, ui)
        assert play_game.valid_input("1") == True
        assert play_game.valid_input("0") == False

    def test_taken_turns_count(self):
        board = Mock()
        ui = UI()
        play_game = PlayGame(board, ui)
        dict_sample = {"1": " ", "2": "X", "3": " "}
        assert play_game.taken_turns_count(dict_sample) == 1

    @patch.object(PlayGame, "taken_turns_count")
    def test_current_mark(self, mock_taken_turns_count):
        mock_taken_turns_count.return_value = 3
        board = Mock()
        ui = UI()
        play_game = PlayGame(board, ui)
        assert play_game.current_mark() == "O"

    @patch.object(UI, "display")
    def test_display_player_turn(self, mock_display):
        board = Mock()
        ui = UI()
        play_game = PlayGame(board, ui)
        play_game.display_player_turn("X")
        mock_display.assert_called_with("It's O's turn")
