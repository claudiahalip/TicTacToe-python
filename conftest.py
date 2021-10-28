from pytest import fixture
import pytest
import mock
from mock import patch
from mock import Mock
from .lib.human_player import HumanPlayer
from .lib.board import Board
from .lib.game import Game
from .lib.tictactoe_board import TicTacToeBoard
from .lib.ui import UI


@fixture(scope="function")
def game_object():
    ui = UI()
    board = TicTacToeBoard(ui)
    player1 = HumanPlayer("X")
    player2 = HumanPlayer("O")
    game = Game(board, ui, player1, player2)
    return game

@fixture(scope="function")
def game_object_with_mock_board():
    board = Mock(win_combinations=[])
    ui = UI()
    player1 = HumanPlayer("X")
    player2 = HumanPlayer("O")
    game = Game(board, ui, player1, player2)
    return game

@fixture(scope="function")
def game_object_with_X_on_position_3():
    ui = UI()
    board = TicTacToeBoard(ui)
    player1 = HumanPlayer("X")
    player2 = HumanPlayer("O")
    game = Game(board, ui, player1, player2)
    board.move("3", "X")
    return game

@fixture(scope="function")
def game_object_with_board_0_win():
    ui = UI()
    board = TicTacToeBoard(ui)
    board.board = {
        1: "O",
        2: "O",
        3: "O",
        4: "X",
        5: "X",
        6: "O",
        7: "X",
        8: "X",
        9: "O",
    }
    player1 = HumanPlayer("X")
    player2 = HumanPlayer("O")
    game = Game(board, ui, player1, player2)
    return game

@fixture(scope="function")
def game_object_with_board_X_win():
    ui = UI()
    board = TicTacToeBoard(ui)
    player1 = HumanPlayer("X")
    player2 = HumanPlayer("O")
    game = Game(board, ui, player1, player2)
    board.board = {
        1: "X",
        2: "X",
        3: "X",
        4: "O",
        5: "O",
        6: "X",
        7: "O",
        8: "O",
        9: "X",
    }
    return game

@fixture(scope="function")
def game_object_with_board_draw():
    ui = UI()
    board = TicTacToeBoard(ui)
    player1 = HumanPlayer("X")
    player2 = HumanPlayer("O")
    game = Game(board, ui, player1, player2)
    board.board = {
        1: "X",
        2: "X",
        3: "O",
        4: "O",
        5: "O",
        6: "X",
        7: "X",
        8: "O",
        9: "X",
    }
    return game

@fixture(scope="function")
def game_object_with_unfull_board():
    ui = UI()
    board = TicTacToeBoard(ui)
    player1 = HumanPlayer("X")
    player2 = HumanPlayer("O")
    game = Game(board, ui, player1, player2)
    board.board = {
        1: "X",
        2: "X",
        3: "O",
        4: "O",
        5: "O",
        6: "X",
        7: "X",
        8: "O",
        9: " ",
    }
    return game

@fixture(scope="function")
def board_object():
    ui = UI()
    board = Board(ui)
    return board

@fixture(scope="function")
def tictactoe_board_object():
    ui = UI()
    board = TicTacToeBoard(ui)
    return board
