import numpy as np
import unittest
import gate

class TestGate(unittest.TestCase):
	def test_is_unitary(self):
		qg = gate.QuantumGate(np.matrix('0 1; 1 0', np.complex_))
		self.assertTrue(qg.is_unitary())

	def test_is_not_unitary(self):
		matrix = np.matrix('1 1; 1 0', np.complex_)
		self.failUnlessRaises(Exception, gate.QuantumGate, matrix)

if __name__ == '__main__':
    unittest.main()
