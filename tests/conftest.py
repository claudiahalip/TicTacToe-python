from pytest import fixture
import pytest
import mock
from mock import patch
from mock import Mock

from lib.game_selection import GameSelection
from lib.human_player import HumanPlayer
from lib.board import Board
from lib.game import Game
from lib.tictactoe_board import TicTacToeBoard
from lib.ui import UI

# game objects
@fixture(scope="function")
def game_object():
    ui = UI()
    board = TicTacToeBoard(ui)
    players = [HumanPlayer(ui, board, "X"), HumanPlayer(ui, board, "O")]
    game = Game(board, ui, players)
    return game


@fixture(scope="function")
def game_object_with_1_empty_space_board():
    ui = UI()
    board = TicTacToeBoard(ui)
    board.board = {
        1: "X",
        2: "O",
        3: "O",
        4: "O",
        5: "O",
        6: "X",
        7: "X",
        8: "O",
        9: "X",
    }
    players = [HumanPlayer(ui, board, "X"), HumanPlayer(ui, board, "O")]
    game = Game(board, ui, players)
    return game


@fixture(scope="function")
def game_object_with_X_on_position_3():
    ui = UI()
    board = TicTacToeBoard(ui)
    players = [HumanPlayer(ui, board, "X"), HumanPlayer(ui, board, "O")]
    game = Game(board, ui, players)
    board.mark_position("3", "X")
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
    players = [HumanPlayer(ui, board, "X"), HumanPlayer(ui, board, "O")]
    game = Game(board, ui, players)
    return game


@fixture(scope="function")
def game_object_with_board_X_win():
    ui = UI()
    board = TicTacToeBoard(ui)
    players = [HumanPlayer(ui, board, "X"), HumanPlayer(ui, board, "O")]
    game = Game(board, ui, players)
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
    players = [HumanPlayer(ui, board, "X"), HumanPlayer(ui, board, "O")]
    game = Game(board, ui, players)
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
    players = [HumanPlayer(ui, board, "X"), HumanPlayer(ui, board, "O")]
    game = Game(board, ui, players)
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
def game_object_with_board_X_win_on_4x4_board():
    ui = UI()
    board = TicTacToeBoard(ui, 4)
    players = [HumanPlayer(ui, board, "X"), HumanPlayer(ui, board, "O")]
    game = Game(board, ui, players)
    board.board = {
        1: "X",
        2: "X",
        3: "X",
        4: "X",
        5: "X",
        6: "X",
        7: "O",
        8: "O",
        9: "X",
        10: "X",
        11: "O",
        12: "X",
        13: "O",
        14: "X",
        15: "O",
        16: "X",
    }
    return game


@fixture(scope="function")
def game_object_with_draw_board_on_4x4_board():
    ui = UI()
    board = TicTacToeBoard(ui, 4)
    players = [HumanPlayer(ui, board, "X"), HumanPlayer(ui, board, "O")]
    game = Game(board, ui, players)
    board.board = {
        1: "X",
        2: "X",
        3: "X",
        4: "0",
        5: "O",
        6: "O",
        7: "O",
        8: "X",
        9: "X",
        10: "O",
        11: "X",
        12: "O",
        13: "X",
        14: "X",
        15: "O",
        16: "X",
    }
    return game


@fixture(scope="function")
def game_object_with_4x4_board():
    ui = UI()
    board = TicTacToeBoard(ui, 4)
    players = [HumanPlayer(ui, board, "X"), HumanPlayer(ui, board, "O")]
    game = Game(board, ui, players)
    return game


# board objects
@fixture(scope="function")
def board_object():
    ui = UI()
    board = Board(ui)
    return board


@fixture(scope="function")
def board_object_with_3X3():
    ui = UI()
    board = Board(ui)
    return board


@fixture(scope="function")
def board_object_with_4X4():
    ui = UI()
    board = TicTacToeBoard(ui, 4)
    return board


@fixture(scope="function")
def tictactoe_board_object():
    ui = UI()
    board = TicTacToeBoard(ui)
    return board


@fixture(scope="function")
def game_selection_object():
    ui = UI()
    board = Board(ui)
    game_selection = GameSelection(ui, board)
    return game_selection


@fixture(scope="function")
def player_object():
    ui = UI()
    board = TicTacToeBoard(ui)
    board.mark_position("4", "X")
    mark = "X"
    player = HumanPlayer(ui, board, mark)
    return player
