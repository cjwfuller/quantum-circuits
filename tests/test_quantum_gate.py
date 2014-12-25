import unittest
import numpy as np
import gates.cnot as cnot

class TestQuantumGate(unittest.TestCase):
    def test_basic_resize(self):
        """Re-sizing a gate by making it act on more qubits, works"""
        gate = cnot.CNOTQuantumGate()
        gate.resize(3, [0, 2])
        shape = np.shape(gate.matrix)
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
            """, np.complex_).all(), gate.matrix.all())

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
        shape = np.shape(gate.matrix)
        size = shape[0]
        self.assertEquals(4, size)
        self.assertEquals(np.matrix("""
            1 0 0 0;
            0 1 0 0;
            0 0 0 1;
            0 0 1 0
        """, np.complex_).all(), gate.matrix.all())

if __name__ == '__main__':
    unittest.main()