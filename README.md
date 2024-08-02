# Finite State Machine - Modulo Three Calculation
## Overview
This project implements a Finite State Machine (FSM) to compute the remainder of an unsigned binary integer when
divided by three. The FSM transitions between states based on binary input and uses these states to determine the
remainder.

## Components
### 'fsm.py'
#### FSM Class:
##### Manages the Fsm states and transitions.
##### Contains methods for state transitions based on binary input strings.
##### Computes the remainder of the binary number when divided by three.

#### 'mod_three' Function:
##### Utilizes FSM to calculate the remainder of a given binary string.
##### Handles invalid input by raising and managing exceptions.

#### 'exceptions.py'
##### 'InvalidInputError' - Exception used to indicate an invalid input (Not '0' or '1')

#### 'test_mod_three.py'
##### Test suite for 'mod_three'

#### 'test_fsm.py'
#### Test suite for FSM class

## Notes
Used nested dictionaries for representing transitions between states rather than using if and elif conditional 
statements. I felt as this would reduce the repeated code in this assignment.
