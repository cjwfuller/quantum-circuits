import math
import numpy as np

class QuantumGate:
    def __init__(self, name):
        if name == 'paulix':
            self.symbol = 'X'
            self.matrix = np.matrix('0 1; 1 0', np.complex_)
        elif name == 'pauliy':
            self.symbol = 'Y'
            self.matrix = np.matrix('0 -1i; 1i 0', np.complex_)
        elif name == 'pauliz':
            self.symbol = 'Z'
            self.matrix = np.matrix('1 0; 0 -1', np.complex_)
        elif name == 'swap':
            self.symbol = 'S'
            self.matrix = np.matrix('1 0 0 0; 0 0 1 0; 0 1 0 0; 0 0 0 1', np.complex_)
        elif name == 'cnot':
            self.symbol = 'C'
            self.matrix = np.matrix('1 0 0 0; 0 1 0 0; 0 0 0 1; 0 0 1 0', np.complex_)
        elif name == 'hadamard':
            self.symbol = 'H'
            self.matrix = ((1/math.sqrt(2)+0j) * np.matrix('1 1; 1 -1', np.complex_))
        elif name == 'toffoli':
            self.symbol = 'T'
            self.matrix = np.matrix(
            '1 0 0 0 0 0 0 0;'
            '0 1 0 0 0 0 0 0;'
            '0 0 1 0 0 0 0 0;'
            '0 0 0 1 0 0 0 0;'
            '0 0 0 0 1 0 0 0;'
            '0 0 0 0 0 1 0 0;'
            '0 0 0 0 0 0 0 1;'
            '0 0 0 0 0 0 1 0', np.complex_
        )
        else:
            raise Exception("Supplied gate name is unknown")

        if(not self.__is_unitary()):
            raise Exception("Supplied matrix is not unitary")

    def __is_unitary(self):
        shape = np.shape(self.matrix)
        # unitary matrices will always have dimension n*n
        x, y = shape[0], shape[1]
        if(x != y):
            return False
        # unitary matrices must satisfy U*U = UU* = I
        identity = np.identity(x)
        conjugate_transpose = self.matrix.getH()
        return (self.matrix * conjugate_transpose).all() == identity.all()


        
