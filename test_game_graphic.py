from unittest.mock import patch
from unittest import TestCase
from dialogue_and_scripts import game_graphic
import io


class TestGame_graphic(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_game_graphic(self, mock_stdout):
        game_graphic()
        expected_stdout = '@@@@@@@@@@@@@@@@@@@@@@@#/////((*,,,,*/*.....,*/////(((' \
                          '////////////(%#%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
        self.assertIn(expected_stdout, mock_stdout.getvalue())
