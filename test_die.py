from unittest import TestCase
from die import Die
import random


class TestDie(TestCase):

    def setUp(self):
        self.test_die = Die(6)

    def test_get_face_value(self):
        die = self.test_die
        expected = 1
        actual = die.get_face_value()
        self.assertEqual(expected, actual)

    def test_get_face_value_after_first_roll(self):
        die = self.test_die
        random.seed(5)
        die.roll_die()
        expected = 5
        actual = die.get_face_value()
        self.assertEqual(expected, actual)

    def test_change_face_value(self):
        die = self.test_die
        die.change_face_value(3)
        expected = 3
        actual = die.get_face_value()
        self.assertEqual(expected, actual)

    def test_change_face_value_less_than_one(self):
        die = self.test_die
        expected = 'New face value cannot be less than 1.'
        actual = die.change_face_value(-2)
        self.assertEqual(expected, actual)

    def test_change_face_value_greater_than_number_of_sides(self):
        die = self.test_die
        expected = 'New face value cannot exceed number of sides.'
        actual = die.change_face_value(8)
        self.assertEqual(expected, actual)

    def test_get_number_of_sides(self):
        die = self.test_die
        expected = 6
        actual = die.get_number_of_sides()
        self.assertEqual(expected, actual)

    def test_change_number_of_sides(self):
        die = self.test_die
        die.change_number_of_sides(8)
        expected = 8
        actual = self.test_die.get_number_of_sides()
        self.assertEqual(expected, actual)

    def test_change_number_of_sides_less_than_2(self):
        die = self.test_die
        expected = 'Number of sides cannot be less than 2.'
        actual = die.change_number_of_sides(0)
        self.assertEqual(expected, actual)

    def test_roll_die(self):
        die = self.test_die
        random.seed(9)
        die.roll_die()
        expected = 4
        actual = die.get_face_value()
        self.assertEqual(expected, actual)
