from ..lib.game import *
from ..lib.ui import *
from ..lib.tictactoe_board import *
import pytest
import mock
from mock import patch
from mock import Mock


class TestGame:
    @patch.object(UI, "display")
    def test_display_board_method_was_called(self, game_object):
        with patch.object(TicTacToeBoard, "display_board") as mock_display_board:
            game_object.start()
        mock_display_board.assert_called

    def test_display_if_O_won(self, game_object_with_board_0_win):
        with patch.object(UI, "display", autospect=True) as mock_display:
            game_object_with_board_0_win.start()
        mock_display.assert_any_call("Game over! O is the winner.")

    def test_display_if_X_won(self, game_object_with_board_X_win):
        with patch.object(UI, "display", autospect=True) as mock_display:
            game_object_with_board_X_win.start()
        mock_display.assert_any_call("Game over! X is the winner.")

    def test_display_if_is_a_draw(self, game_object_with_board_draw):
        with patch.object(UI, "display", autospect=True) as mock_display:
            game_object_with_board_draw.start()
        mock_display.assert_any_call("Game over! It's a draw.")

    def test_take_turns_method_was_called(self, game_object_with_mock_board):
        with patch.object(Game, "take_turns", autospec=True) as mock_take_turns:
            game_object_with_mock_board.start()
        mock_take_turns.assert_called

    def test_switch_players_for_next_player_method(self, game_object):
        game_object.switch_players()
        assert game_object.current_player.mark == "O"

    # tests for is_over method
    def test_is_over_when_the_board_is_full(self, game_object_with_board_draw):
        assert game_object_with_board_draw.is_over() == True

    def test_is_over_when_there_is_a_winner(self, game_object_with_board_X_win):
        assert game_object_with_board_X_win.is_over() == True

    def test_is_not_over_when_the_board_is_not_full(
        self, game_object_with_unfull_board
    ):
        assert game_object_with_unfull_board.is_over() == False

    # tests for is_a_win method
    def test_is_a_win_return_win_combination_if_a_winner(
        self, game_object_with_board_X_win
    ):
        assert game_object_with_board_X_win.is_a_win() == True

    def test_is_a_win_return_false_if_no_winner(self, game_object_with_board_draw):
        assert game_object_with_board_draw.is_a_win() == False
