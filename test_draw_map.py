from unittest import TestCase
from unittest.mock import patch
from character import Character
from map_and_movement import draw_map
import io


class TestDraw_map(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_draw_map_coordinates_top_border(self, mock_stdout):
        test_character = Character('Josh', 10, [3, 3], 0)
        expected_stdout = '\no - - - - o \n|         | \n|         | \n|     X   | \n|         | \no - - - - o \n'
        draw_map(test_character)
        self.assertEqual(expected_stdout, mock_stdout.getvalue())

