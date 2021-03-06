import math

import unittest2 as unittest
import numpy as np

import register as r

class TestRegister(unittest.TestCase):

    def test_basic_construction(self):
        """Constructing a valid register with no superposition, works"""
        state = np.array([1, 0], dtype=np.complex_)
        register = r.Register(1, state)

    def test_superposition_construction(self):
        """Constructing a valid register with superposition, works"""
        state = np.array([1/math.sqrt(2), 1/math.sqrt(2)], dtype=np.complex_)
        register = r.Register(1, state)

    def test_invalid_size_constraint(self):
        """Constructing register with invalid size, fails"""
        state = np.array([0, 1, 0], dtype=np.complex_)
        self.assertRaises(Exception, r.Register, state, 2)

    def test_invalid_state_constraint(self):
        """Constructing register with invalid state, fails"""
        state = np.array([1, 1, 1, 1], dtype=np.complex_)
        self.assertRaises(Exception, r.Register, state, 2)

    def test_basic_generate_bases(self):
        """Generating bases for a 3-qubit system results in the correct
        bases
        """
        expected_bases = [[0, 0, 0], [0, 0, 1],[0, 1, 0], [0, 1, 1], [1, 0, 0],
                [1, 0, 1], [1, 1, 0], [1, 1, 1]]
        generated_bases = r.Register.generate_bases(3)
        self.assertEquals(expected_bases, generated_bases)

    def test_generate_single_qubit_bases(self):
        """Generating bases for a 1-qubit system results in the correct
        bases
        """
        expected_bases = [[0], [1]]
        generated_bases = r.Register.generate_bases(1)
        self.assertEquals(expected_bases, generated_bases)

    def test_basic_filter(self):
        """Filtering a 3-qubit to qubits 0 and 2, works"""
        expected_filtered = [[0, 0], [0, 1], [0, 0], [0, 1], [1, 0], [1, 1],
                [1, 0], [1, 1]]
        actual_filtered = r.Register.filter_bases(3, [0, 2])
        self.assertEquals(expected_filtered, actual_filtered)

    def test_filter_whole_system(self):
        """Filtering all qubits, works"""
        expected_filtered = [[0, 0, 0], [0, 0, 1],[0, 1, 0], [0, 1, 1],
                [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
        actual_filtered = r.Register.filter_bases(3, [0, 1, 2])
        self.assertEquals(expected_filtered, actual_filtered)

    def test_filter_non_existant_qubit(self):
        """Filtering a with a qubit that doesn't exist, fails"""
        self.assertRaises(Exception, r.Register.filter_bases, 3, [0, 4])

    def test_two_qubit_dirac_to_column_conversion(self):
        """Converting 2-qubit Dirac vectors to column vectors, works"""
        vectors = {
                (0, 0): [0, 0, 0, 1],
                (0, 1): [0, 0, 1, 0],
                (1, 0): [0, 1, 0, 0],
                (1, 1): [1, 0, 0, 0],
        }
        for key, value in vectors.items():
            actual_converted = r.Register.dirac_to_column_vector(key)
            self.assertEquals(value, actual_converted)

    def test_three_qubit_dirac_to_column_conversion(self):
        """Converting 3-qubit Dirac vectors to column vectors, works"""
        vectors = {
                (0, 0, 0): [0, 0, 0, 0, 0, 0, 0, 1],
                (0, 0, 1): [0, 0, 0, 0, 0, 0, 1, 0],
                (0, 1, 0): [0, 0, 0, 0, 0, 1, 0, 0],
                (0, 1, 1): [0, 0, 0, 0, 1, 0, 0, 0],
                (1, 0, 0): [0, 0, 0, 1, 0, 0, 0, 0],
                (1, 0, 1): [0, 0, 1, 0, 0, 0, 0, 0],
                (1, 1, 0): [0, 1, 0, 0, 0, 0, 0, 0],
                (1, 1, 1): [1, 0, 0, 0, 0, 0, 0, 0],
        }
        for key, value in vectors.items():
            actual_converted = r.Register.dirac_to_column_vector(key)
            self.assertEquals(value, actual_converted)

    def test_smallest_column_to_dirac_conversion(self):
        """Converting from [0, 0, 0, 0] to |00>, works"""
        actual_converted = r.Register.column_vector_to_possible_dirac_vectors(
                [0, 0, 0, 1]
        )
        expected_converted = [[0, 0]]
        self.assertEquals(expected_converted, actual_converted)

    def test_basic_column_vector_to_possible_dirac_vectors_conversion(self):
        """Converting from [0, 0, 1, 0] to |01>, works"""
        actual_converted = r.Register.column_vector_to_possible_dirac_vectors(
                [0, 0, 1, 0]
        )
        expected_converted = [[0, 1]]
        self.assertEquals(expected_converted, actual_converted)

    def test_largest_column_to_dirac_conversion(self):
        """Converting from [1, 0, 0, 0] to |11>, works"""
        actual_converted = r.Register.column_vector_to_possible_dirac_vectors(
                [1, 0, 0, 0]
        )
        expected_converted = [[1, 1]]
        self.assertEquals(expected_converted, actual_converted)

    def test_more_than_one_possible_dirac_conversion(self):
        """Converting from a column vector with more than one possible Dirac
        vector, works"""
        actual_converted = r.Register.column_vector_to_possible_dirac_vectors(
                [1/math.sqrt(2), 0, 0, 1/math.sqrt(2)]
        )
        expected_converted = [[0, 0], [1, 1]]
        for expected in expected_converted:
            self.assertTrue(expected in actual_converted)

if __name__ == '__main__':
    unittest.main()