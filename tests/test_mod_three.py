"""
test_mod_three.py

This module contains unit tests for the mod_three function. It includes tests for:
- Base cases with one character.
- Empty string input.
- Exception handling for invalid characters and types.
- Valid binary strings and their expected remainders.
- Movement through all FSM states with various input combinations.
"""
import unittest
from fsm import mod_three
from exceptions import InvalidInputError


class TestModThree(unittest.TestCase):
    """
    Unit tests for the mod_three function.

    Tests:
    - Base cases with one character.
    - Empty string input.
    - Exception handling for invalid characters and types.
    - Valid binary strings and their expected remainders.
    - Movement through all FSM states with various input combinations.
    """
    def test_base_case_one_char(self):
        """
        Test base cases with single character binary strings '0' and '1'.
        """
        self.assertEqual(mod_three('0'), 0)
        self.assertEqual(mod_three('1'), 1)

    def test_empty_string(self):
        """
        Test handling of an empty string input, which should return the state it in.
        :return:
        """
        self.assertEqual(mod_three(''), 0)

    def test_exception_handling(self):
        """
        Test exception handling for various inputs.
        """
        with self.assertRaises(InvalidInputError):
            mod_three('a')
        with self.assertRaises(InvalidInputError):
            mod_three('1s')
        with self.assertRaises(InvalidInputError):
            mod_three('1013')
        with self.assertRaises(InvalidInputError):
            mod_three('0d1')
        with self.assertRaises(InvalidInputError):
            mod_three('10090')
        with self.assertRaises(TypeError):
            mod_three(0)
        with self.assertRaises(TypeError):
            mod_three(1)
        with self.assertRaises(TypeError):
            mod_three(1011)

    def test_valid_inputs(self):
        """
        Test cases where there are valid inputs.
        """
        self.assertEqual(mod_three('1101'), 1)
        self.assertEqual(mod_three('1110'), 2)
        self.assertEqual(mod_three('1111'), 0)

    def test_movement_through_all_paths(self):
        """
        Test cases that go through all possible paths in the FSM.
        :return:
        """
        self.assertEqual(mod_three('0101010'), 0)
        self.assertEqual(mod_three('01'), 1)
        self.assertEqual(mod_three('10'), 2)
        self.assertEqual(mod_three('101'), 2)
        self.assertEqual(mod_three('1010'), 1)


if __name__ == '__main__':
    unittest.main()
