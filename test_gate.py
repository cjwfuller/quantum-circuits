import numpy as np
import unittest
import gate

class TestGate(unittest.TestCase):
    def test_paulix_is_unitary(self):
        qg = gate.QuantumGate(np.matrix('0 1; 1 0', np.complex_))

    def test_pauliy_is_unitary(self):
        qg = gate.QuantumGate(np.matrix('0 -1i; 1i 0', np.complex_))

    def test_pauliz_is_unitary(self):
        qg = gate.QuantumGate(np.matrix('1 0; 0 -1', np.complex_))

    def test_swap_is_unitary(self):
        qg = gate.QuantumGate(np.matrix('1 0 0 0; 0 0 1 0; 0 1 0 0; 0 0 0 1', np.complex_))

    def test_cnot_is_unitary(self):
        qg = gate.QuantumGate(np.matrix('1 0 0 0; 0 1 0 0; 0 0 0 1; 0 0 1 0', np.complex_))

    def test_toffoli_is_unitary(self):
        toffoli = np.matrix(
            '1 0 0 0 0 0 0 0;'
            '0 1 0 0 0 0 0 0;'
            '0 0 1 0 0 0 0 0;'
            '0 0 0 1 0 0 0 0;'
            '0 0 0 0 1 0 0 0;'
            '0 0 0 0 0 1 0 0;'
            '0 0 0 0 0 0 0 1;'
            '0 0 0 0 0 0 1 0', np.complex_
        )
        qg = gate.QuantumGate(toffoli)

    def test_is_not_unitary(self):
        matrix = np.matrix('1 1; 1 0', np.complex_)
        self.failUnlessRaises(Exception, gate.QuantumGate, matrix)

    def test_complex_is_not_unitary(self):
        matrix = np.matrix('1 -1i; 1 -1i', np.complex_)
        self.failUnlessRaises(Exception, gate.QuantumGate, matrix)

if __name__ == '__main__':
    unittest.main()
