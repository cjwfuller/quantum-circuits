import unittest
import gate

class TestGate(unittest.TestCase):

    def test_construction_constraint(self):
        """Directly instantiating a QuantumGate, fails"""
        self.assertRaises(TypeError, gate.Gate)

if __name__ == '__main__':
    unittest.main()