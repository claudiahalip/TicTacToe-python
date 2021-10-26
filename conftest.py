from pytest import fixture

from .lib.board import Board
from .lib.game import Game
from .lib.ui import UI
from .lib.tictactoe_board import *
import mock
from mock import patch
from mock import Mock


@fixture(scope="function")
def game_object():
    board = Mock(win_combinations=[])
    ui = UI()
    game = Game(board, ui)
    return game