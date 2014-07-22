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

    def test_implemented_gates_only_constraint(self):
        self.assertRaises(Exception, gate.QuantumGate, 'foo')

    def test_gates_have_alphabetic_symbols(self):
        paulix = gate.QuantumGate('paulix')
        self.assertEquals('X', paulix.symbol)

        pauliy = gate.QuantumGate('pauliy')
        self.assertEquals('Y', pauliy.symbol)

        pauliz = gate.QuantumGate('pauliz')
        self.assertEquals('Z', pauliz.symbol)

        swap = gate.QuantumGate('swap')
        self.assertEquals('S', swap.symbol)

        cnot = gate.QuantumGate('cnot')
        self.assertEquals('C', cnot.symbol)

        toffoli = gate.QuantumGate('toffoli')
        self.assertEquals('T', toffoli.symbol)

        hadamard = gate.QuantumGate('hadamard')
        self.assertEquals('H', hadamard.symbol)

if __name__ == '__main__':
    unittest.main()
