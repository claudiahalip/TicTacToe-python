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
    def test_computer_input(self):
        ui = UI()
        board = TicTacToeBoard(ui)
        computer_player = ComputerPlayer(ui, board, "X")
        assert computer_player.computer_input() == 1
