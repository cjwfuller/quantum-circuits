import numpy as np

class QuantumGate:
    def __init__(self, matrix):
        self.matrix = matrix
        if(not self.__is_unitary()):
            raise Exception("Supplied matrix is not unitary")

    def __is_unitary(self):
        shape = np.shape(self.matrix)
        # unitary matrices will always have dimension n*n
        x, y = shape[0], shape[1]
        if(x != y):
            return False
        # unitary matrices must satisfy U*U = UU* = I
        identity = self.matrix.getI()
        conjugate_transpose = self.matrix.getH()
        return (self.matrix * conjugate_transpose).all() == identity.all()
