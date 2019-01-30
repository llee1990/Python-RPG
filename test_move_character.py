from unittest import TestCase
from character import Character
from map_and_movement import move_character


class TestMove_character(TestCase):

    def test_move_character_north(self):
        test_character = Character('Chris', 10, [2, 2], 0)
        actual_return = move_character(test_character, 'N')
        expected_return = True
        expected_coordinates = [1, 2]
        actual_coordinates = test_character.get_coordinate()
        self.assertEqual(expected_return,actual_return)
        self.assertEqual(expected_coordinates, actual_coordinates)

    def test_move_character_south(self):
        test_character = Character('Chris', 10, [2, 2], 0)
        actual_return = move_character(test_character, 'S')
        expected_return = True
        expected_coordinates = [3, 2]
        actual_coordinates = test_character.get_coordinate()
        self.assertEqual(expected_return,actual_return)
        self.assertEqual(expected_coordinates, actual_coordinates)

    def test_move_character_east(self):
        test_character = Character('Chris', 10, [2, 2], 0)
        actual_return = move_character(test_character, 'E')
        expected_return = True
        expected_coordinates = [2, 3]
        actual_coordinates = test_character.get_coordinate()
        self.assertEqual(expected_return,actual_return)
        self.assertEqual(expected_coordinates, actual_coordinates)

    def test_move_character_west(self):
        test_character = Character('Chris', 10, [2, 2], 0)
        actual_return = move_character(test_character, 'W')
        expected_return = True
        expected_coordinates = [2, 1]
        actual_coordinates = test_character.get_coordinate()
        self.assertEqual(expected_return,actual_return)
        self.assertEqual(expected_coordinates, actual_coordinates)

    def test_move_character_lower_boundary(self):
        test_character = Character('Chris', 10, [1, 2], 0)
        actual_return = move_character(test_character, 'N')
        expected_return = False
        expected_coordinates = [1, 2]
        actual_coordinates = test_character.get_coordinate()
        self.assertEqual(expected_return,actual_return)
        self.assertEqual(expected_coordinates, actual_coordinates)

    def test_move_character_upper_boundary(self):
        test_character = Character('Chris', 10, [1, 4], 0)
        actual_return = move_character(test_character, 'E')
        expected_return = False
        expected_coordinates = [1, 4]
        actual_coordinates = test_character.get_coordinate()
        self.assertEqual(expected_return,actual_return)
        self.assertEqual(expected_coordinates, actual_coordinates)
