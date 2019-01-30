from unittest import TestCase
from character import Character
from enemy import Child
import random


class TestCharacter(TestCase):

    def setUp(self):
        self.test_character = Character('Daniel', 10, [2, 3], 0)
        self.test_enemy = Child(5)

    def test_get_name(self):
        expected = 'Daniel'
        actual = self.test_character.get_name()
        self.assertEqual(expected, actual)

    def test_get_health(self):
        expected = 10
        actual = self.test_character.get_health()
        self.assertEqual(expected, actual)

    def test_get_health_after_attack(self):
        random.seed(4)
        self.test_enemy.attack(self.test_character)
        expected = 8
        actual = self.test_character.get_health()
        self.assertEqual(expected, actual)

    def test_get_damage(self):
        expected = 0
        actual = self.test_character.get_damage()
        self.assertEqual(expected, actual)

    def test_get_damage_after_one_round_of_battle(self):
        random.seed(4)
        self.test_character.attack(self.test_enemy)
        expected = 2
        actual = self.test_character.get_damage()
        self.assertEqual(expected, actual)

    def test_get_kill_count_base(self):
        expected = 0
        actual = self.test_character.get_kill_count()
        self.assertEqual(expected, actual)

    def test_get_kill_count_after_kill(self):
        self.test_character.add_kill()
        expected = 1
        actual = self.test_character.get_kill_count()
        self.assertEqual(expected, actual)

    def test_get_coordinate(self):
        expected = [2, 3]
        actual = self.test_character.get_coordinate()
        self.assertEqual(expected, actual)

    def test_add_kill(self):
        self.test_character.add_kill()
        expected = 1
        actual = self.test_character.get_kill_count()
        self.assertEqual(expected, actual)

    def test_regenerate_one_health_full_health(self):
        self.test_character.regenerate_one_health()
        expected = 10
        actual = self.test_character.get_health()
        self.assertEqual(expected, actual)

    def test_regenerate_one_health_partial_health(self):
        self.test_character.decrease_health(5)
        self.test_character.regenerate_one_health()
        expected = 6
        actual = self.test_character.get_health()
        self.assertEqual(expected, actual)

    def test_decrease_health(self):
        self.test_character.decrease_health(4)
        expected_hp = 6
        actual_hp = self.test_character.get_health()
        self.assertEqual(expected_hp, actual_hp)

    def test_decrease_health_max_damage(self):
        self.test_character.decrease_health(6)
        expected_hp = 4
        actual_hp = self.test_character.get_health()
        self.assertEqual(expected_hp, actual_hp)

    def test_decrease_health_negative(self):
        self.test_character.decrease_health(20)
        expected_hp = -10
        actual_hp = self.test_character.get_health()
        self.assertEqual(expected_hp, actual_hp)

    def test_set_health(self):
        self.test_character.set_health(2)
        expected = 2
        actual = self.test_character.get_health()
        self.assertEqual(expected, actual)

    def test_set_zero_health(self):
        self.test_character.set_zero_health()
        expected = 0
        actual = self.test_character.get_health()
        self.assertEqual(expected, actual)

    def test_set_coordinate(self):
        self.test_character.set_coordinate([3, 3])
        expected = [3, 3]
        actual = [3, 3]
        self.assertEqual(expected, actual)

    def test_move_north(self):
        self.test_character.move('N')
        expected = [1, 3]
        actual = self.test_character.get_coordinate()
        self.assertEqual(expected, actual)

    def test_move_south(self):
        self.test_character.move('S')
        expected = [3, 3]
        actual = self.test_character.get_coordinate()
        self.assertEqual(expected, actual)

    def test_move_east(self):
        self.test_character.move('E')
        expected = [2, 4]
        actual = self.test_character.get_coordinate()
        self.assertEqual(expected, actual)

    def test_move_west(self):
        self.test_character.move('W')
        expected = [2, 2]
        actual = self.test_character.get_coordinate()
        self.assertEqual(expected, actual)

    def test_attack(self):
        random.seed(1)
        self.test_character.attack(self.test_enemy)
        expected_damage = 2
        expected_enemy_health = 3
        actual_damage = self.test_character.get_damage()
        actual_enemy_health = self.test_enemy.get_health()
        self.assertEqual(expected_damage, actual_damage)
        self.assertEqual(expected_enemy_health, actual_enemy_health)

    def test_attack_hp_less_than_zero(self):
        self.test_character.set_health(-2)
        expected = None
        actual = self.test_character.attack(self.test_enemy)
        self.assertEqual(expected, actual)
