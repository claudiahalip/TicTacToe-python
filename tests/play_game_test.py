from ..lib.play_game import *
from ..lib.board import *
from ..lib.ui import *

import mock
from mock import patch
from mock import Mock


class TestPlayGame:
    def test_test1(self):
        assert True

    def test_display_welcome_message(self):
        board = Board()
        ui = UI()
        with patch.object(UI, "display", autospect=True) as mock_display:
            play_game = PlayGame(board, ui)
            play_game.start()
        mock_display.assert_called_with("Welcome to TIC TAC TOE!")

    def test_display_board(self):
        board = Board()
        ui = UI()
        with patch.object(Board, "display_board", autospect=True) as mock_display_board:
            play_game = PlayGame(board, ui)
            play_game.start()
        mock_display_board.assert_called()
        
    
