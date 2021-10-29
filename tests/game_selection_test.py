import pytest
import mock
from mock import patch
from mock import Mock
from ..lib.ui import UI
from ..lib.game_selection import *


class TestGameSelections:
    @patch.object(UI, "get_user_input", side_effect=["a,", "c"])
    def test_display_method_was_called(self, mock_input, game_selection_object):
        with patch.object(UI, "display", autospect=True) as mock_display:
            game_selection_object.select_game_type()
        mock_display.assert_any_call("Welcome to TIC TAC TOE!")
