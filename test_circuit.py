import unittest
import circuit

class TestCircuit(unittest.TestCase):
    def test_initialise_size(self):
        c = circuit.Circuit(3, 10)

if __name__ == '__main__':
    unittest.main()