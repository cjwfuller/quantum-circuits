import numpy as np

class QuantumGate:
    def __init__(self, matrix):
        self.matrix = matrix
        if(not self.is_unitary()):
            raise Exception("Supplied matrix is not unitary")

    # TODO
    def is_unitary(self):
        shape = np.shape(self.matrix)
        # unitary matrices will always have dimension n*n
        x = shape[0]
        y = shape[1]
        if(x != y):
            return False
        # unitary matrices must satisfy U*U = UU* = I
        identity = self.matrix.getI
        conjugate_transpose = self.matrix.getH
        print identity
        # FIXME
        return (self.matrix * conjugate_transpose) == identity

if __name__ == '__main__':
    qg = QuantumGate(np.matrix('0 1; 1 0'))