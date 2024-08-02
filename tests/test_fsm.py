"""
test_fsm.py

This module contains unit tests for the FSM class. It includes tests for:
- Initial state of the FSM.
- State transitions for various inputs.
- Handling of invalid inputs.
- Correct computations of remainders based on the FSM's state.
"""
import unittest
from fsm import FSM
from exceptions import InvalidInputError


class TestFSM(unittest.TestCase):
    """
    Unit tests for the FSM class.

    Tests:
    - Initial state of the FSM.
    - Transitions between states for invalid inputs.
    - Handling of invalid inputs.
    - State remainders and correct computation.
    """

    def setUp(self):
        self.fsm = FSM()

    def test_initial_state(self):
        """
        Test that the FSM starts in the initial state 'S0'.
        :return:
        """
        self.assertEqual(self.fsm.state, 'S0')

    def test_transition_from_S0(self):
        """
        Test state transitions from the initial state 'S0'.
        """
        self.fsm.transition('0')
        self.assertEqual(self.fsm.state, 'S0')
        self.fsm.transition('1')
        self.assertEqual(self.fsm.state, 'S1')

    def test_transition_from_S1(self):
        """
        Test state transitions from the state 'S1'.
        """
        self.fsm.transition('1')
        self.fsm.transition('0')
        self.assertEqual(self.fsm.state, 'S2')
        self.fsm.transition('1')
        self.assertEqual(self.fsm.state, 'S2')
        self.fsm.transition('0')
        self.assertEqual(self.fsm.state, 'S1')

    def test_transition_from_S2(self):
        """
        Test state transitions from the state 'S2'.
        """
        self.fsm.transition('1')
        self.fsm.transition('0')
        self.assertEqual(self.fsm.state, 'S2')
        self.fsm.transition('1')
        self.assertEqual(self.fsm.state, 'S2')
        self.fsm.transition('0')
        self.assertEqual(self.fsm.state, 'S1')

    def test_invalid_input(self):
        """
        Test handling of invalid input characters.
        """
        with self.assertRaises(InvalidInputError):
            self.fsm.transition('2')

        with self.assertRaises(InvalidInputError):
            self.fsm.transition('')

        with self.assertRaises(InvalidInputError):
            self.fsm.transition('x')

        with self.assertRaises(InvalidInputError):
            self.fsm.transition(0)

        with self.assertRaises(InvalidInputError):
            self.fsm.transition(1)

        with self.assertRaises(InvalidInputError):
            self.fsm.transition(1011)

    def test_long_input(self):
        """
        Test state transition of a long binary string input that goes through all possible transition paths.
        """
        self.fsm.transition('1')
        self.fsm.transition('0')
        self.fsm.transition('1')
        self.fsm.transition('0')
        self.fsm.transition('1')
        self.fsm.transition('0')
        self.fsm.transition('1')
        self.fsm.transition('0')
        self.assertEqual(self.fsm.get_remainder(), 2)

    def test_state_remainders(self):
        """
        Test translation of state into modulo three remainders for all possible states.
        """
        self.assertEqual(self.fsm.get_remainder(), 0)
        self.fsm.transition('0')
        self.assertEqual(self.fsm.get_remainder(), 0)
        self.fsm.transition('1')
        self.assertEqual(self.fsm.get_remainder(), 1)
        self.fsm.transition('1')
        self.assertEqual(self.fsm.get_remainder(), 0)
        self.fsm.transition('1')
        self.fsm.transition('0')
        self.assertEqual(self.fsm.get_remainder(), 2)
        self.fsm.transition('1')
        self.assertEqual(self.fsm.get_remainder(), 2)
        self.fsm.transition('0')
        self.assertEqual(self.fsm.get_remainder(), 1)


if __name__ == '__main__':
    unittest.main()
