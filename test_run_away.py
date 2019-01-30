from unittest.mock import patch
from unittest import TestCase
from character import Character
import combat
from enemy import Child
import io

class TestRun_away(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('die.Die.roll_die', return_value=1)
    def test_run_away_take_damage(self, mock_rolldie, mock_stdout):
        test_character = Character('Chi', 10, [1, 2], 0)
        test_enemy = Child(5)
        combat.run_away(test_character, test_enemy)
        expected_stdout = "You have escaped, but have taken " + str(test_enemy.get_escape_damage()) + " points of "
        "damage in the process. You now have " + str(test_character.get_health()) + " health points remaining."
        self.assertIn(expected_stdout, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('die.Die.roll_die', return_value=4)
    def test_run_away_no_damage(self, mock_rolldie, mock_stdout):
        test_character = Character('Chi', 10, [1, 2], 0)
        test_enemy = Child(5)
        combat.run_away(test_character, test_enemy)
        expected_stdout = "You have escaped unscathed, the child runs off into the darkness."
        self.assertIn(expected_stdout, mock_stdout.getvalue())
