from unittest.mock import patch
from unittest import TestCase
from character import Character
import character_creation
import save_and_load
import io


class TestExisting_character_detected(TestCase):

    @patch('builtins.input', return_value='')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_existing_character_detected_overwrite(self, mock_stdout, mock_input):
        expected_test_character = Character('John', 10, [1, 3], 0)
        actual_character = character_creation.existing_character_detected('John', 'W')
        expected_stdout = 'My...my name is...'
        self.assertEqual(expected_test_character.get_name(), actual_character.get_name())
        self.assertEqual(expected_test_character.get_health(), actual_character.get_health())
        self.assertEqual(expected_test_character.get_coordinate(), actual_character.get_coordinate())
        self.assertEqual(expected_test_character.get_kill_count(), actual_character.get_kill_count())
        self.assertIn(expected_stdout, mock_stdout.getvalue())

    def test_existing_character_detected_load(self):
        expected_test_character = Character('Peter', 10, [1, 3], 0)
        save_and_load.save_game(expected_test_character)
        actual_character = character_creation.existing_character_detected('Peter', 'L')
        self.assertEqual(expected_test_character.get_name(), actual_character.get_name())
        self.assertEqual(expected_test_character.get_health(), actual_character.get_health())
        self.assertEqual(expected_test_character.get_coordinate(), actual_character.get_coordinate())
        self.assertEqual(expected_test_character.get_kill_count(), actual_character.get_kill_count())
        save_and_load.do_not_save(expected_test_character)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_existing_character_detected_invalid_command(self, mock_stdout):
        character_creation.existing_character_detected('John', 'das324ksa')
        expected_stdout = 'That is not a valid command.'
        self.assertIn(expected_stdout, mock_stdout.getvalue())
