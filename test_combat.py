from unittest.mock import patch
from unittest import TestCase
from character import Character
import combat
import io


class TestCombat(TestCase):

    @patch('enemy.Child.get_health', return_value=0)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_kill_enemy_die(self, mock_stdout, mock_enemy):
        test_character = Character('Wayne', 10, [2, 3], 0)
        combat.combat(test_character)
        expected_stdout = "You find the scent of fresh blood oddly aromatic"
        expected_kill_count = 1
        actual_kill_count = test_character.get_kill_count()
        self.assertIn(expected_stdout, mock_stdout.getvalue())
        self.assertEqual(expected_kill_count, actual_kill_count)

    @patch('character.Character.get_health', return_value=0)
    @patch('enemy.Child.get_health', return_value=20)
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value='N')
    def test_combat_kill_character_die(self, mock_input, mock_stdout, mock_enemy, mock_character):
        test_character = Character('Wayne', 10, [2, 3], 0)
        with self.assertRaises(SystemExit):
            combat.combat(test_character)
            expected_stdout = "You have been killed by a child. What kind of serial killer are you? Game Over.\n"
            expected_hp = 0
            actual_hp = test_character.get_health()
            self.assertIn(expected_stdout, mock_stdout.getvalue())
            self.assertEqual(expected_hp, actual_hp)

    @patch('enemy.Child.get_health', return_value=20)
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value='N')
    def test_combat_kill_character_enemy_continue_battle(self, mock_input, mock_stdout, mock_enemy):
        test_character = Character('Wayne', 10, [2, 3], 0)
        with self.assertRaises(SystemExit):
            combat.combat(test_character)
            expected_stdout = 'The child is persistent! She continues to shoot you with the'
            expected_stdout_2 = 'You stab the screaming child again and do'
            self.assertIn(expected_stdout, mock_stdout.getvalue())
            self.assertIn(expected_stdout_2, mock_stdout.getvalue())

