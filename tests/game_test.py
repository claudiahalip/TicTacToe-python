from ..lib.game import Game
from ..lib.game import *
from ..lib.board import *
from ..lib.ui import *
from ..lib.tictactoe_board import *
import pytest
import mock
from mock import patch
from mock import Mock


class TestGame:
    def test_display_method_was_called(self):
        board = Mock(win_combinations=[])
        ui = UI()
        with patch.object(UI, "display", autospect=True) as mock_display:
            game = Game(board, ui)
            game.start()
        mock_display.assert_called

    def test_display_board_method_was_called(self):
        board = Mock(win_combinations=[])
        ui = UI()
        with patch.object(
            TicTacToeBoard, "display_board", autospect=True
        ) as mock_display_board:
            game = Game(board, ui)
            game.start()
        mock_display_board.assert_called

    def test_display_if_O_won(self):
        ui = UI()
        board = TicTacToeBoard(ui)
        game = Game(board, ui)
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
        with patch.object(UI, "display", autospect=True) as mock_display:
            game = Game(board, ui)
            game.start()
        mock_display.assert_any_call("Game over! O is the winner.")

    def test_display_if_X_won(self):
        ui = UI()
        board = TicTacToeBoard(ui)
        game = Game(board, ui)
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
        with patch.object(UI, "display", autospect=True) as mock_display:
            game = Game(board, ui)
            game.start()
        mock_display.assert_any_call("Game over! X is the winner.")

    def test_display_if_is_a_draw(self):
        ui = UI()
        board = TicTacToeBoard(ui)
        game = Game(board, ui)
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
        with patch.object(UI, "display", autospect=True) as mock_display:
            game = Game(board, ui)
            game.start()
        mock_display.assert_any_call("Game over! It's a draw.")

    def test_take_turns_method_was_called(self):
        ui = UI()
        board = Mock(win_combinations=[])
        with patch.object(Game, "take_turns", autospec=True) as mock_take_turns:
            game = Game(board, ui)
            game.start()
            mock_take_turns.assert_called

    # #tests for take_turns method
    # True, true
    @patch.object(UI, "get_user_input", side_effect=["2", "3"])
    @patch.object(TicTacToeBoard, "display_board")
    @patch.object(TicTacToeBoard, "move")
    def test_the_take_turns_when_the_input_is_valid_and_the_position_is_not_taken(
        self, mock_input, mock_move, mock_display_board
    ):
        ui = UI()
        board = TicTacToeBoard(ui)
        game = Game(board, ui)
        game.take_turns("X")
        mock_move.assert_called_once()
        mock_display_board.assert_called_once()

    # True, false
    @patch.object(UI, "get_user_input", side_effect=["3", "2"])
    @patch.object(UI, "display")
    def test_the_take_turns_when_the_input_is_valid_and_the_position_is_taken(
        self, mock_display, mock_input
    ):
        ui = UI()
        board = TicTacToeBoard(ui)
        game = Game(board, ui)
        board.move("3", "X")
        game.take_turns("X")
        mock_display.assert_any_call("Invalid number")

    # False, true
    @patch.object(UI, "get_user_input", side_effect=["0", "2"])
    @patch.object(UI, "display")
    def test_the_take_turns_when_the_input_is_not_valid_and_the_position_is_not_taken(
        self, mock_display, mock_input
    ):
        ui = UI()
        board = TicTacToeBoard(ui)
        game = Game(board, ui)
        game.take_turns("X")
        mock_display.assert_any_call("Invalid number")

    # false, false
    @patch.object(UI, "get_user_input", side_effect=["0", "3", "2"])
    @patch.object(UI, "display")
    def test_the_take_turns_when_the_input_is_not_valid_and_the_position_is_taken(
        self, mock_display, mock_input
    ):
        ui = UI()
        board = TicTacToeBoard(ui)
        game = Game(board, ui)
        board.move("3", "X")
        game.take_turns("X")
        mock_display.assert_any_call("Invalid number")

    @pytest.mark.parametrize("input, expected", [("1", True), ("0", False)])
    def test_valid_input(self, input, expected):
        ui = UI()
        new_board = Board(ui)
        game = Game(new_board, ui)
        assert game.valid_input(input) == expected

    def test_switch_players_for_next_player_method(self):
        ui = UI()
        board = Board(ui)
        game = Game(board, ui)
        game.switch_players()
        assert game.current_player == "O"

    # tests for is_over method
    def test_is_over_when_the_board_is_full(self):
        ui = Mock()
        board = Board(ui)
        # draw board
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
        game = Game(board, ui)
        assert game.is_over() == True

    def test_is_over_when_there_is_a_winner(self):
        ui = Mock()
        board = Board(ui)
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
        game = Game(board, ui)
        assert game.is_over() == True

    def test_is_not_over_when_the_board_is_not_full(self):
        ui = Mock()
        board = TicTacToeBoard(ui)
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
        game = Game(board, ui)
        assert game.is_over() == False

    # tests for is_a_win method
    def test_is_a_win_return_win_combination_if_a_winner(self):
        ui = UI()
        board = TicTacToeBoard(ui)
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
        game = Game(board, ui)
        assert game.is_a_win() == True

    def test_is_a_win_return_false_if_no_winner(self):
        ui = UI()
        board = TicTacToeBoard(ui)
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
        game = Game(board, ui)
        assert game.is_a_win() == False
