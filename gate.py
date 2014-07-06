import numpy as np

class QuantumGate:
    def __init__(self, matrix):
        self.matrix = matrix
        if(not self.is_unitary()):
            raise Exception("Supplied matrix is not unitary")

    def is_unitary(self):
        shape = np.shape(self.matrix)
        # unitary matrixes should have dimension n * n
        x = shape[0]
        y = shape[1]
        if(x != y):
            return False
        # TODO
        identity = np.identity(x, np.complex_)
        conjugate_transpose = self.matrix
        return True

if __name__ == '__main__':
    qg = QuantumGate([[0,1],[1,0]])