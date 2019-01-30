from unittest.mock import patch
from unittest import TestCase
from save_and_load import restart_or_quit
import io


class TestRestart_or_quit(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value='dwada')
    def test_jihyo(self, mock_input, mock_stdout):
        expected_stdout = 'That is not a valid command.'
        restart_or_quit()
        self.assertIn(expected_stdout, mock_stdout.getvalue())

    @patch('builtins.input', return_value='N')
    def test_restart_or_quit_exit_game(self, mock_input):
        with self.assertRaises(SystemExit):
            restart_or_quit()

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['Y', 'N'])
    def test_restart_or_quit_wrong_input(self, mock_stdout, mock_input):
        with self.assertRaises(SystemExit):
            restart_or_quit()
