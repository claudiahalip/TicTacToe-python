import pytest
import mock
from mock import patch
from mock import Mock

from ..lib.computer_player import ComputerPlayer

from ..lib.human_player import HumanPlayer
from ..lib.game import *
from ..lib.ui import *
from ..lib.tictactoe_board import *


class TestComputerPlayer:
    def test_next_available_space_index_when_borad_is_empty(self):
        ui = UI()
        board = TicTacToeBoard(ui)
        computer_player = ComputerPlayer(board, "X")
        assert computer_player.next_available_space_index() == 1

    def test_next_available_space_index_when_board_is_partially_full(self):
        ui = UI()
        board = TicTacToeBoard(ui)
        board.board = board.board = {
            1: "X",
            2: "X",
            3: "O",
            4: " ",
            5: "O",
            6: "X",
            7: "X",
            8: "O",
            9: " ",
        }
        computer_player = ComputerPlayer(board, "X")
        assert computer_player.next_available_space_index() == 4
