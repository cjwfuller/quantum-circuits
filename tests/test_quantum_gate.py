import unittest

import numpy as np

import quantum_gate
import gates.cnot as cnot

class TestQuantumGate(unittest.TestCase):

    def test_construction_constraint(self):
        """Directly instantiating a QuantumGate, fails"""
        self.assertRaises(TypeError, quantum_gate.QuantumGate)

    def test_basic_resize(self):
        """Re-sizing a gate by making it act on more qubits, works"""
        gate = cnot.CNOTQuantumGate()
        gate.resize(3, [0, 2])
        shape = np.shape(gate.get_matrix())
        size = shape[0]
        self.assertEquals(8, size)
        self.assertEquals(np.matrix("""
               1 0 0 0 0 0 0 0;
               0 1 0 0 0 0 0 0;
               0 0 1 0 0 0 0 0;
               0 0 0 1 0 0 0 0;
               0 0 0 0 0 1 0 0;
               0 0 0 0 1 0 0 0;
               0 0 0 0 0 0 0 1;
               0 0 0 0 0 0 1 0
            """, np.complex_).all(), gate.get_matrix().all())

    def test_resize_different_qubit_order(self):
        """Re-sizing and specifying qubits not in order, works"""
        gate = cnot.CNOTQuantumGate()
        gate.resize(3, [2, 0])
        shape = np.shape(gate.get_matrix())
        size = shape[0]
        self.assertEquals(8, size)
        self.assertEquals(np.matrix("""
               1 0 0 0 0 0 0 0;
               0 1 0 0 0 0 0 0;
               0 0 1 0 0 0 0 0;
               0 0 0 1 0 0 0 0;
               0 0 0 0 0 1 0 0;
               0 0 0 0 1 0 0 0;
               0 0 0 0 0 0 0 1;
               0 0 0 0 0 0 1 0
            """, np.complex_).all(), gate.get_matrix().all())

    def test_resize_too_few_qubit_nums_constraint(self):
        """Re-sizing and specifying too few qubits, fails

        When re-sizing an n-qubit gate, n qubit numbers should be specified
        """
        gate = cnot.CNOTQuantumGate()
        self.assertRaises(ValueError, gate.resize, 3, [1])

    def test_resize_too_many_qubit_nums_constraint(self):
        """Re-sizing and specifying too many qubits, fails

        When re-sizing an n-qubit gate, n qubit numbers should be specified
        """
        gate = cnot.CNOTQuantumGate()
        self.assertRaises(ValueError, gate.resize, 3, [0, 1, 2])

    def test_non_integer_components_gate_reize(self):
        """Re-sizing a gate with non-integer real/imaginary components,
        works"""

    def test_shrink_constraint(self):
        """Making an n-qubit gate act on m whith m < n, fails"""
        gate = cnot.CNOTQuantumGate()
        self.assertRaises(Exception, gate.resize, 1, [0, 2])

    def test_non_resize(self):
        """Re-sizing an n-qubit gate to an n-qubit gate does nothing to the
        gate"""
        gate = cnot.CNOTQuantumGate()
        gate.resize(2, [0, 1])
        shape = np.shape(gate.get_matrix())
        size = shape[0]
        self.assertEquals(4, size)
        self.assertEquals(np.matrix("""
            1 0 0 0;
            0 1 0 0;
            0 0 0 1;
            0 0 1 0
        """, np.complex_).all(), gate.get_matrix().all())

if __name__ == '__main__':
    unittest.main()