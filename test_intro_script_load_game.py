from unittest.mock import patch
from unittest import TestCase
from character import Character
from dialogue_and_scripts import intro_script_load_game
import io


class TestIntro_script_load_game(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_intro_script_load_game_is_player_name_called(self, mock_stdout):
        test_character = Character('Leon', 10, [1, 2], 0)
        intro_script_load_game(test_character)
        expected_stdout = 'Leon'
        self.assertIn(expected_stdout, mock_stdout.getvalue())
