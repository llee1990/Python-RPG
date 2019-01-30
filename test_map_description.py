from unittest.mock import patch
from unittest import TestCase
from character import Character
import dialogue_and_scripts
import io


class TestMap_description(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_map_description_position_1_1(self, mock_stdout):
        test_character = Character('Jihyo', 10, [1, 1], 0)
        dialogue_and_scripts.map_description(test_character)
        expected_stdout = "You are at the northwest corner of the house. You feel weird facing a corner."
        self.assertIn(expected_stdout, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_map_description_position_1_2(self, mock_stdout):
        test_character = Character('Jihyo', 10, [1, 2], 0)
        dialogue_and_scripts.map_description(test_character)
        expected_stdout = "You enter the living room, looks like a cozy home..."
        self.assertIn(expected_stdout, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_map_description_position_1_3(self, mock_stdout):
        test_character = Character('Jihyo', 10, [1, 3], 0)
        dialogue_and_scripts.map_description(test_character)
        expected_stdout = "This is the entrance to the house. Through the shadows you can "
        "see the living room to your west and a small bedroom to your east."
        self.assertIn(expected_stdout, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_map_description_position_1_4(self, mock_stdout):
        test_character = Character('Jihyo', 10, [1, 4], 0)
        dialogue_and_scripts.map_description(test_character)
        expected_stdout = "This is a bedroom, it is small. Perhaps it belonged to a child."
        self.assertIn(expected_stdout, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_map_description_position_2_1(self, mock_stdout):
        test_character = Character('Jihyo', 10, [2, 1], 0)
        dialogue_and_scripts.map_description(test_character)
        expected_stdout = "Snacks and tea are on the living room table, the tea is still steaming..."
        self.assertIn(expected_stdout, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_map_description_position_2_2(self, mock_stdout):
        test_character = Character('Jihyo', 10, [2, 2], 0)
        dialogue_and_scripts.map_description(test_character)
        expected_stdout = "There is a big TV in this living room. You stop and stare into the reflection.\n"
        "A masked figure mask stares back."
        self.assertIn(expected_stdout, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_map_description_position_2_3(self, mock_stdout):
        test_character = Character('Jihyo', 10, [2, 3], 0)
        dialogue_and_scripts.map_description(test_character)
        expected_stdout = "You are near the center of the house, a photo of a family hangs on the wall. "
        "Where can they be hiding..."
        self.assertIn(expected_stdout, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_map_description_position_2_4(self, mock_stdout):
        test_character = Character('Jihyo', 10, [2, 4], 0)
        dialogue_and_scripts.map_description(test_character)
        expected_stdout = "This bedroom is small, there is a bunk bed against the wall littered with stuffed animals."
        self.assertIn(expected_stdout, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_map_description_position_3_1(self, mock_stdout):
        test_character = Character('Jihyo', 10, [3, 1], 0)
        dialogue_and_scripts.map_description(test_character)
        expected_stdout = "You are between the living room and the kitchen. A small window overlooks the garden."
        self.assertIn(expected_stdout, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_map_description_position_3_2(self, mock_stdout):
        test_character = Character('Jihyo', 10, [3, 2], 0)
        dialogue_and_scripts.map_description(test_character)
        expected_stdout = "You are between the living room and the kitchen. The living room is to your north"
        " and to the south is the kitchen."
        self.assertIn(expected_stdout, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_map_description_position_3_3(self, mock_stdout):
        test_character = Character('Jihyo', 10, [3, 3], 0)
        dialogue_and_scripts.map_description(test_character)
        expected_stdout = "You look around the house, to the south is the master bedroom."
        self.assertIn(expected_stdout, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_map_description_position_3_4(self, mock_stdout):
        test_character = Character('Jihyo', 10, [3, 4], 0)
        dialogue_and_scripts.map_description(test_character)
        expected_stdout = "You look outside the window, there is a full moon tonight."
        self.assertIn(expected_stdout, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_map_description_position_4_1(self, mock_stdout):
        test_character = Character('Jihyo', 10, [4, 1], 0)
        dialogue_and_scripts.map_description(test_character)
        expected_stdout = "You enter the kitchen and opened one of the cabinets, "
        "considering to choose another weapon.\nYou decided to stick with the kitchen knife."
        self.assertIn(expected_stdout, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_map_description_position_4_2(self, mock_stdout):
        test_character = Character('Jihyo', 10, [4, 2], 0)
        dialogue_and_scripts.map_description(test_character)
        expected_stdout = "You look around and open the refrigerator, there are some leftover spaghetti and meatloaf."
        self.assertIn(expected_stdout, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_map_description_position_4_3(self, mock_stdout):
        test_character = Character('Jihyo', 10, [4, 3], 0)
        dialogue_and_scripts.map_description(test_character)
        expected_stdout = "This is the master bedroom. There is a king-sized bed with maroon bedsheets."
        "They smelled like they had just been changed."
        self.assertIn(expected_stdout, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_map_description_position_4_4(self, mock_stdout):
        test_character = Character('Jihyo', 10, [4, 4], 0)
        dialogue_and_scripts.map_description(test_character)
        expected_stdout = "You open the walk-in closet in the master bedroom. Perhaps they are hiding here..."
        self.assertIn(expected_stdout, mock_stdout.getvalue())
