"""
fsm.py

This module implements a Finite State Machine (FSM) for determining the remainder when a binary string is divided by
three. It contains the FSM class with methods for state transitions and remainder calculation. The mod_three function
uses the FSM class to calculate the remainder of a given binary string.

Classes:
- FSM: Represents a Finite State Machine with methods to transition to states and calculate the remainder.

Functions:
- mod_three(binary_string): Computes the remainder when a binary string is divided by three

Exceptions:
- InvalidInputError: Raised when an invalid input character is encountered.
"""
from exceptions import InvalidInputError

STATE_S0 = 'S0'
STATE_S1 = 'S1'
STATE_S2 = 'S2'
ZERO_DIGIT = '0'
ONE_DIGIT = '1'
ZERO = 0
ONE = 1
TWO = 2


class FSM:
    """
    Finite State Machine for computing the remainder when a binary string is divided by three

    Attributes:
    state (str): Current state of FSM, starting with 'S0'.
    transitions (dict): A nested dictionary mapping each state and input to the next state.
    remainder (dict): A dictionary mapping each state to its corresponding remainder

    Methods:
    transition(input_char): Updates the FMS state based on the input character.
    get_remainder(): Returns the remainder based on the current state.
    """
    def __init__(self):
        self.state = 'S0'

        self.transitions = {
            STATE_S0: {ZERO_DIGIT: STATE_S0, ONE_DIGIT: STATE_S1},
            STATE_S1: {ZERO_DIGIT: STATE_S2, ONE_DIGIT: STATE_S0},
            STATE_S2: {ZERO_DIGIT: STATE_S1, ONE_DIGIT: STATE_S2}
        }

        self.remainder = {
            STATE_S0: ZERO,
            STATE_S1: ONE,
            STATE_S2: TWO
        }

    def transition(self, input_char):
        """
        Update the FSM state based on the input character.

        :param input_char: The input character string ('0' or '1') to transition the state.
        :raises Invalid InputError: If the input character is not '0' or '1'.
        """
        if input_char not in {ZERO_DIGIT, ONE_DIGIT}:
            raise InvalidInputError(f"Invalid character '{input_char}' is not the expected '0' or '1'!")
        self.state = self.transitions[self.state][input_char]

    def get_remainder(self):
        """
        Get the remainder value based on the current FSM state.

        :return: The remainder value (0, 1, or 2) as an integer corresponding to the current state.
        """
        return self.remainder[self.state]


def mod_three(binary_string):
    """
    Calculate the remainder when the binary string is divided by three using an FSM.

    :param binary_string: The binary string to process.
    :return: The remainder as an integer when the binary string is divided by three.
    :raises: InvalidInputError if the binary string contains characters other than '0' or '1' and TypeError is the type
    is not a string.
    """
    fsm = FSM()
    for char in binary_string:
        try:
            fsm.transition(char)
        except InvalidInputError as e:
            print(f"Error: {e}")
            raise
    return fsm.get_remainder()
