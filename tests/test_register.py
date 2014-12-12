import math
import unittest
import numpy as np
import register

class TestRegister(unittest.TestCase):

    def test_basic_construction(self):
        """Constructing a valid register with no superposition, works"""
        state = np.array([1, 0], dtype=np.complex_)
        r = register.Register(1, state)

    def test_superposition_construction(self):
        """Constructing a valid register with superposition, works"""
        state = np.array([1/math.sqrt(2), 1/math.sqrt(2)], dtype=np.complex_)
        r = register.Register(1, state)

    def test_invalid_size_constraint(self):
        """Constructing register with invalid size, fails"""
        state = np.array([0, 1, 0], dtype=np.complex_)
        self.assertRaises(Exception, register.Register, state, 2)

    def test_invalid_state_constraint(self):
        """Constructing register with invalid state, fails"""
        state = np.array([1, 1, 1, 1], dtype=np.complex_)
        self.assertRaises(Exception, register.Register, state, 2)

if __name__ == '__main__':
    unittest.main()