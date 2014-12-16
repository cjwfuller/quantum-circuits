import numpy as np
import gate

class PauliXQuantumGate(gate.QuantumGate):
    def __init__(self):
        self.symbol = 'X'
        self.matrix = np.matrix('0 1; 1 0', np.complex_)

    def get_symbol(self):
        return self.symbol

    def get_matrix(self):
        return self.matrix
