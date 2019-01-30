from unittest.mock import patch
from unittest import TestCase
from character import Character
from dialogue_and_scripts import intro_script
import io

class TestIntro_script(TestCase):

    @patch('builtins.input', side_effect=['', ''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_intro_script_is_player_name_called(self, mock_stdout, mock_input):
        test_character = Character('Leon', 10, [1, 2], 0)
        intro_script(test_character)
        expected_stdout = 'Leon'
        self.assertIn(expected_stdout, mock_stdout.getvalue())
