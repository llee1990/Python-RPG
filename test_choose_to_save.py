from unittest.mock import patch
from unittest import TestCase
from character import Character
from save_and_load import choose_to_save, do_not_save, load_game, save_game
import json
import io


class TestChoose_to_save(TestCase):

    @patch('builtins.input', return_value='Y')
    def test_choose_to_save_yes(self, mock_input):
        test_character = Character('Test_save', 10, [1, 3], 0)
        choose_to_save(test_character)
        test_file = 'Test_save.json'
        with open(test_file) as file_object:
            test_stats = json.load(file_object)
            self.assertEqual(['Test_save', 10, [1, 3], 0], [test_stats['name'], test_stats['health'],
                                                            test_stats['coordinates'], test_stats['kills']])
        do_not_save(test_character)

    @patch('builtins.input', return_value='N')
    def test_choose_to_save_no(self, mock_input):
        test_character = Character('Test_do_not_save', 10, [1, 3], 0)
        save_game(test_character)
        choose_to_save(test_character)
        test_loaded_character = load_game('Test_do_not_save')
        self.assertEqual(False, test_loaded_character)

    @patch('builtins.input', side_effect=['asdad', 'N'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_to_save_wrong_input(self, mock_stdout, mock_input):
        test_character = Character('Test_do_not_save', 10, [1, 3], 0)
        save_game(test_character)
        choose_to_save(test_character)
        expected_stdout = 'That is not a valid command.'
        self.assertIn(expected_stdout, mock_stdout.getvalue())
