from unittest.mock import patch
from unittest import TestCase
import combat
import io
from character import Character


class TestFight_or_run(TestCase):

    @patch('builtins.input', return_value="Fight")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_fight_or_run_fight(self, mock_stdout, mock_input):
        test_character = Character('Jihyo', 10, [1, 3], 0)
        expected_std_out = '\nYou stab the screaming child'
        combat.fight_or_run(test_character)
        self.assertIn(expected_std_out, mock_stdout.getvalue())

    @patch('builtins.input', return_value="Run")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_fight_or_run_run(self, mock_std, mock_input):
        test_character = Character('Jihyo', 10, [1, 3], 0)
        expected_std_out = '\nYou walk away, the thought of killing a child was too much for you. ' \
                           'But in her fear the child attempts to attack you!'
        combat.fight_or_run(test_character)
        self.assertIn(expected_std_out, mock_std.getvalue())

    @patch('builtins.input', side_effect=["asdjsjkdal", "Fight"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_fight_or_run_wrong_input(self, mock_std, mock_input):
        test_character = Character('Jihyo', 10, [1, 3], 0)
        expected_std_out = "You have not entered a valid command."
        combat.fight_or_run(test_character)
        self.assertIn(expected_std_out, mock_std.getvalue())
