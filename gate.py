import math
import numpy as np

class QuantumGate:
    def __init__(self, name):
        if name == 'paulix':
            self.matrix = self.__get_paulix()
            self.symbol = 'X'
        elif name == 'pauliy':
            self.matrix = self.__get_pauliy()
            self.symbol = 'Y'
        elif name == 'pauliz':
            self.matrix = self.__get_pauliz()
            self.symbol = 'Z'
        elif name == 'swap':
            self.matrix = self.__get_swap()
            self.symbol = 'S'
        elif name == 'cnot':
            self.matrix = self.__get_cnot()
            self.symbol = 'C'
        elif name == 'toffoli':
            self.matrix = self.__get_toffoli()
            self.symbol = 'T'
        elif name == 'hadamard':
            self.matrix = self.__get_hadamard()
            self.symbol = 'H'
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

    def __get_paulix(self):
        return np.matrix('0 1; 1 0', np.complex_)

    def __get_pauliy(self):
        return np.matrix('0 -1i; 1i 0', np.complex_)

    def __get_pauliz(self):
        return np.matrix('1 0; 0 -1', np.complex_)

    def __get_swap(self):
        return np.matrix('1 0 0 0; 0 0 1 0; 0 1 0 0; 0 0 0 1', np.complex_)

    def __get_hadamard(self):
        return ((1/math.sqrt(2)+0j) * np.matrix('1 1; 1 -1', np.complex_))

    def __get_cnot(self):
        return np.matrix('1 0 0 0; 0 1 0 0; 0 0 0 1; 0 0 1 0', np.complex_)

    def __get_toffoli(self):
        return np.matrix(
            '1 0 0 0 0 0 0 0;'
            '0 1 0 0 0 0 0 0;'
            '0 0 1 0 0 0 0 0;'
            '0 0 0 1 0 0 0 0;'
            '0 0 0 0 1 0 0 0;'
            '0 0 0 0 0 1 0 0;'
            '0 0 0 0 0 0 0 1;'
            '0 0 0 0 0 0 1 0', np.complex_
        )
