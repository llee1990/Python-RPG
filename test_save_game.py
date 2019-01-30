from unittest import TestCase
from save_and_load import save_game, do_not_save
from character import Character
import json


class TestSave_game(TestCase):

    def test_save_game(self):
        test_character = Character('Test_save', 10, [1, 3], 0)
        save_game(test_character)
        test_file = 'Test_save.json'
        with open(test_file) as file_object:
            test_stats = json.load(file_object)
            self.assertEqual(['Test_save', 10, [1, 3], 0], [test_stats['name'], test_stats['health'],
                             test_stats['coordinates'], test_stats['kills']])
        do_not_save(test_character)


