from unittest.mock import patch
from unittest import TestCase
import comp_1510_a1
from character import Character
from save_and_load import save_game, do_not_save
import io


class TestStart_game(TestCase):

    @patch('builtins.input', return_value='N')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_start_game_under_18(self, mock_stdout, mock_input):
        with self.assertRaises(SystemExit):
            comp_1510_a1.start_game()
            expected_stdout = "DISCLAIMER: This game is rated 'M' for MATURE, are you over 18? (Y / N)"
            self.assertIn(expected_stdout, mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['asdjasjkhd', 'N'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_start_game_invalid_command(self, mock_stdout, mock_input):
        with self.assertRaises(SystemExit):
            comp_1510_a1.start_game()
            expected_stdout = "That is not a valid command."
            self.assertIn(expected_stdout, mock_stdout.getvalue())

    @patch('character_creation.create_character', return_value=Character('Kevin', 10, [1, 3], 0))
    @patch('builtins.input', side_effect=['Y', 'N'])
    def test_start_game_start_new_game(self, mock_input, mock_character):
        test_character = Character('Kevin', 10, [1, 3], 0)
        save_game(test_character)
        actual_character = comp_1510_a1.start_game()
        self.assertEqual(test_character.get_name(), actual_character.get_name())
        self.assertEqual(test_character.get_health(), actual_character.get_health())
        self.assertEqual(test_character.get_coordinate(), actual_character.get_coordinate())
        self.assertEqual(test_character.get_kill_count(), actual_character.get_kill_count())
        do_not_save(test_character)

    @patch('builtins.input', side_effect=['Y', 'L', ' Kevin'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_start_game_start_load_game(self, mock_stdout, mock_input):
        test_character = Character('Kevin', 10, [1, 3], 0)
        save_game(test_character)
        actual_character = comp_1510_a1.start_game()
        expected_stdout = 'I see you could not resist your lust for blood.'
        self.assertIn(expected_stdout, mock_stdout.getvalue())
        self.assertEqual(test_character.get_name(), actual_character.get_name())
        self.assertEqual(test_character.get_health(), actual_character.get_health())
        self.assertEqual(test_character.get_coordinate(), actual_character.get_coordinate())
        self.assertEqual(test_character.get_kill_count(), actual_character.get_kill_count())
        do_not_save(test_character)