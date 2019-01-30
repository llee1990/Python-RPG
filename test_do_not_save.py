from unittest import TestCase
from save_and_load import save_game, do_not_save, load_game
from character import Character


class TestDo_not_save(TestCase):

    def test_do_not_save(self):
        test_character = Character('Test_do_not_save', 10, [1, 3], 0)
        save_game(test_character)
        do_not_save(test_character)
        test_loaded_character = load_game('Test_do_not_save')
        self.assertEqual(False, test_loaded_character)
