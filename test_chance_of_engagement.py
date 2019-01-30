from unittest import TestCase
from unittest.mock import patch
from character import Character
import combat
import io


class TestChance_of_engagement(TestCase):

    @patch('die.Die.roll_die', return_value=2)
    def test_chance_of_engagement_no_monsters(self, mock_rolldie):
        test_character = Character('Ethan', 10, [1, 3], 0)
        test_character.set_health(6)
        combat.chance_of_engagement(test_character)
        expected_hp = 7
        actual_hp = test_character.get_health()
        self.assertEqual(expected_hp, actual_hp)

    @patch('die.Die.roll_die', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value='Fight')
    def test_chance_of_engagement_engage_with_monster(self, mock_input, mock_stdout, mock_rolldie):
        test_character = Character('Ethan', 10, [1, 3], 0)
        test_character.set_health(6)
        combat.chance_of_engagement(test_character)
        expected_stdout = 'You encounter a scared child. She is armed. Will you run or fight?'
        self.assertIn(expected_stdout, mock_stdout.getvalue())
