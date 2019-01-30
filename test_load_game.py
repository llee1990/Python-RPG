from unittest import TestCase
from save_and_load import save_game, load_game, do_not_save
from character import Character


class TestLoad_game(TestCase):

    def test_load_game(self):
        test_character = Character('Test_load', 10, [1, 3], 0)
        save_game(test_character)
        test_load_character = load_game('Test_load')
        self.assertEqual(['Test_load', 10, [1, 3], 0], [test_load_character.get_name(),
                                                        test_load_character.get_health(),
                                                        test_load_character.get_coordinate(),
                                                        test_load_character.get_kill_count()])
        do_not_save(test_character)

    def test_load_game_FileNotFoundError(self):
        test_load = load_game('Non-existent_character')
        self.assertEqual(False, test_load)
