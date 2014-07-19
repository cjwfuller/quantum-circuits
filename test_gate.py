import numpy as np
import unittest
import gate

class TestGate(unittest.TestCase):
    def test_standard_gates_implemented(self):
        gate.QuantumGate('paulix')
        gate.QuantumGate('pauliy')
        gate.QuantumGate('pauliz')
        gate.QuantumGate('swap')
        gate.QuantumGate('cnot')
        gate.QuantumGate('toffoli')
        gate.QuantumGate('hadamard')

if __name__ == '__main__':
    unittest.main()
