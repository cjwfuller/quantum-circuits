from abc import abstractmethod
import math
import numpy as np

class QuantumGate(object):
    @abstractmethod
    def get_symbol():
        pass

    @abstractmethod
    def get_matrix():
        pass

    def __is_unitary(self):
        """Determine whether the gate is unitary"""
        shape = np.shape(self.matrix)
        # unitary matrices will always have dimension n*n
        x, y = shape[0], shape[1]
        if(x != y):
            return False
        # unitary matrices must satisfy U*U = UU* = I
        identity = np.identity(x)
        conjugate_transpose = self.matrix.getH()
        return (self.matrix * conjugate_transpose).all() == identity.all()

    def resize(self, num_qubits):
        """Resize a gate to act on a given number of qubits.

        Gates can act on an arbitrary number of qubits but they must be
        resized so they can be applied to the circuit
        """

