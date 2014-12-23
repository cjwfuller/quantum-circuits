import unittest
import paulix

class TestGate(unittest.TestCase):
    def test_basic_resize(self):
        """Re-sizing a gate by making it act on more qubits, works"""

    def test_non_integer_components_gate_reize(self):
        """Re-sizing a gate with non-integer real/imaginary components,
        works"""

    def test_shrink_constraint(self):
        """Making an n-qubit gate act on m whith m < n, fails"""

    def test_resize_too_large_constraint(self):
        """Re-sizing a gate to n qubits for a qubit system of size m where n >
        m, fails"""

    def test_non_resize(self):
        """Re-sizing an n-qubit gate to an n-qubit gate does nothing to the
        gate"""

if __name__ == '__main__':
    unittest.main()