# Leon Lee
# BCIT
# A01062166
from unittest import TestCase
from character import Character
from enemy import Child
import random


class TestChild(TestCase):

    def setUp(self):
        self.test_character = Character('Jihyo', 10, [1, 2], 0)
        self.test_enemy = Child(5)

    def test_get_health(self):
        expected = 5
        actual = self.test_enemy.get_health()
        self.assertEqual(expected, actual)

    def test_get_health_after_attack(self):
        random.seed(4)
        self.test_character.attack(self.test_enemy)
        expected = 3
        actual = self.test_enemy.get_health()
        self.assertEqual(expected, actual)

    def test_set_zero_health(self):
        self.test_enemy.set_zero_health()
        expected = 0
        actual = self.test_enemy.get_health()
        self.assertEqual(expected, actual)

    def test_get_damage(self):
        expected = 0
        actual = self.test_enemy.get_damage()
        self.assertEqual(expected, actual)

    def test_get_damage_after_first_round_of_battle(self):
        random.seed(7)
        self.test_enemy.attack(self.test_character)
        expected = 3
        actual = self.test_enemy.get_damage()
        self.assertEqual(expected, actual)

    def test_get_escape_damage(self):
        random.seed(7)
        self.test_enemy.escape_attack(self.test_character)
        expected = 3
        actual = self.test_enemy.get_escape_damage()
        self.assertEqual(expected, actual)

    def test_set_health(self):
        self.test_enemy.set_health(3)
        expected = 3
        actual = self.test_enemy.get_health()
        self.assertEqual(expected, actual)

    def test_attack(self):
        random.seed(2)
        self.test_enemy.attack(self.test_character)
        expected_damage = 1
        expected_character_health = 9
        actual_damage = self.test_enemy.get_damage()
        actual_character_health = self.test_character.get_health()
        self.assertEqual(expected_damage, actual_damage)
        self.assertEqual(expected_character_health, actual_character_health)

    def test_escape_attack(self):
        random.seed(4)
        self.test_enemy.escape_attack(self.test_character)
        expected_damage = 2
        expected_character_health = 8
        actual_damage = self.test_enemy.get_escape_damage()
        actual_character_health = self.test_character.get_health()
        self.assertEqual(expected_damage, actual_damage)
        self.assertEqual(expected_character_health, actual_character_health)

    def test_decrease_health(self):
        self.test_enemy.decrease_health(3)
        expected_hp = 2
        actual_hp = self.test_enemy.get_health()
        self.assertEqual(actual_hp, expected_hp)

    def test_decrease_health_until_less_than_0(self):
        self.test_enemy.decrease_health(10)
        expected_hp = -5
        actual_hp = self.test_enemy.get_health()
        self.assertEqual(actual_hp, expected_hp)

    def test_decrease_health_max_damage(self):
        self.test_enemy.decrease_health(6)
        expected_hp = -1
        actual_hp = self.test_enemy.get_health()
        self.assertEqual(actual_hp, expected_hp)
