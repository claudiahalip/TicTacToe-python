import pytest
import mock
from mock import patch
from mock import Mock

from ..lib.computer_player import ComputerPlayer

from ..lib.human_player import HumanPlayer
from ..lib.game import *
from ..lib.ui import *
from ..lib.tictactoe_board import *
from ..lib.ai_computer_player import *


class TestAiComputerPlayer:
    def test_ai_index(self):
        ui = UI()
        board = TicTacToeBoard(ui)
        board.board = {
            1: "X",
            2: " ",
            3: "X",
            4: " ",
            5: "O",
            6: " ",
            7: " ",
            8: " ",
            9: "O",
        }
        computer_player = AiComputerPlayer(board, "X", ui)
        assert computer_player.ai_index() == 2

    def test_ai_index_when_block_a_win_condition(self):
        ui = UI()
        board = TicTacToeBoard(ui)
        board.board = {
            1: "X",
            2: "O",
            3: "X",
            4: " ",
            5: " ",
            6: " ",
            7: " ",
            8: "O",
            9: " ",
        }
        computer_player = AiComputerPlayer(board, "X", ui)
        assert computer_player.ai_index() == 5
