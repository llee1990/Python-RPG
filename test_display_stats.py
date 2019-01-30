from unittest import TestCase
from dialogue_and_scripts import display_stats
from character import Character


class TestDisplay_stats(TestCase):

    def test_display_stats_0_kills(self):
        test_character = Character('Josh', 10, [3, 3], 0)
        expected = '\nYour current HP is 10.\nYou have killed 0 children.'
        actual = display_stats(test_character)
        self.assertEqual(expected, actual)

    def test_display_stats_1_kill(self):
        test_character = Character('Josh', 10, [3, 3], 0)
        test_character.add_kill()
        display_stats(test_character)
        expected = '\nYour current HP is 10.\nYou have killed 1 child.'
        actual = display_stats(test_character)
        self.assertEqual(expected, actual)

    def test_display_stats_10_kills(self):
        test_character = Character('Josh', 10, [3, 3], 10)
        display_stats(test_character)
        expected = '\nYour current HP is 10.\nYou have killed 10 children.'
        actual = display_stats(test_character)
        self.assertEqual(expected, actual)