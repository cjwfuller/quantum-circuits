import unittest
import circuit

class TestCircuit(unittest.TestCase):
    def test_basic_construction(self):
        c = circuit.Circuit(1, 5)

if __name__ == '__main__':
    unittest.main()