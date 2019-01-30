from unittest.mock import patch
from unittest import TestCase
from character import Character
from save_and_load import save_game
from comp_1510_a1 import game_loop
import io


class TestGame_loop(TestCase):

    @patch('builtins.input', side_effect=['Q', 'N'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_game_loop_quit_game(self, mock_stdout, mock_input):
        with self.assertRaises(SystemExit):
            test_character = Character('Test_do_not_save', 10, [1, 3], 0)
            save_game(test_character)
            game_loop(test_character)
            expected_stdout = "Do you want to play again"
            self.assertIn(expected_stdout, mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['asdkjhsajdhajsk', 'Q', 'N'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_game_loop_incorrect_input(self, mock_stdout, mock_input):
        with self.assertRaises(SystemExit):
            test_character = Character('Test', 10, [1, 3], 0)
            save_game(test_character)
            game_loop(test_character)
            expected_stdout = "Do you want to play again"
            self.assertIn(expected_stdout, mock_stdout.getvalue())

    @patch('map_and_movement.move_character', return_value=False)
    @patch('builtins.input', side_effect=['S', 'Q', 'N'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_game_loop_character_move_hit_boundary(self, mock_stdout, mock_input, mock_move_character):
        with self.assertRaises(SystemExit):
            test_character = Character('Test', 10, [1, 3], 0)
            save_game(test_character)
            game_loop(test_character)
        expected_stdout = "You find yourself in a dark house"
        self.assertIn(expected_stdout, mock_stdout.getvalue())

    @patch('map_and_movement.move_character', return_value=True)
    @patch('die.Die.roll_die', return_value=4)
    @patch('builtins.input', side_effect=['S', 'Q', 'N'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_game_loop_character_move_then_quit(self, mock_stdout, mock_input, mock_die, mock_move_character):
        with self.assertRaises(SystemExit):
            test_character = Character('Test', 20, [1, 3], 0)
            save_game(test_character)
            game_loop(test_character)
        expected_stdout = "Quitting so soon..?"
        self.assertIn(expected_stdout, mock_stdout.getvalue())