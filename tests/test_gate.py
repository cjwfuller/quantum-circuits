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

    def test_paulix_symbol(self):
        paulix = gate.QuantumGate('paulix')
        self.assertEquals('X', paulix.symbol)

    def test_pauliy_symbol(self):
        pauliy = gate.QuantumGate('pauliy')
        self.assertEquals('Y', pauliy.symbol)

    def test_pauliz_symbol(self):
        pauliz = gate.QuantumGate('pauliz')
        self.assertEquals('Z', pauliz.symbol)

    def test_swap_symbol(self):
        swap = gate.QuantumGate('swap')
        self.assertEquals('S', swap.symbol)

    def test_cnot_symbol(self):
        cnot = gate.QuantumGate('cnot')
        self.assertEquals('C', cnot.symbol)

    def test_toffoli_symbol(self):
        toffoli = gate.QuantumGate('toffoli')
        self.assertEquals('T', toffoli.symbol)

    def test_hadamard_symbol(self):
        hadamard = gate.QuantumGate('hadamard')
        self.assertEquals('H', hadamard.symbol)

    def test_resize_num_qubits_qubit_nums_constraint(self):
        hadamard = gate.QuantumGate('hadamard')
        self.assertRaises(Exception, hadamard.resize, 2, [0, 1, 2])

if __name__ == '__main__':
    unittest.main()
