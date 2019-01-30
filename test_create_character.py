from unittest.mock import patch
from unittest import TestCase
from character_creation import create_character
from character import Character
from save_and_load import do_not_save, save_game


class TestCreate_character(TestCase):

    @patch('builtins.input', return_value='Bob_New')
    def test_create_character_no_saved_file_found(self, mock_input):
        expected_test_character = Character('Bob_New', 10, [1, 3], 0)
        actual_character = create_character()
        self.assertEqual(expected_test_character.get_name(), actual_character.get_name())
        self.assertEqual(expected_test_character.get_health(), actual_character.get_health())
        self.assertEqual(expected_test_character.get_coordinate(), actual_character.get_coordinate())
        self.assertEqual(expected_test_character.get_kill_count(), actual_character.get_kill_count())
        do_not_save(actual_character)

    @patch('builtins.input', side_effect=['Bob_Old', 'L'])
    def test_create_character_saved_file_found(self, mock_input):
        expected_test_character = Character('Bob_Old', 7, [2, 4], 1)
        save_game(expected_test_character)
        actual_character = create_character()
        self.assertEqual(expected_test_character.get_name(), actual_character.get_name())
        self.assertEqual(expected_test_character.get_health(), actual_character.get_health())
        self.assertEqual(expected_test_character.get_coordinate(), actual_character.get_coordinate())
        self.assertEqual(expected_test_character.get_kill_count(), actual_character.get_kill_count())
        do_not_save(actual_character)