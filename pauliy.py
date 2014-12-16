import numpy as np
import gate

class PauliYQuantumGate(gate.QuantumGate):
    def __init__(self):
        self.symbol = 'Y'
        self.matrix = np.matrix('0 -1i; 1i 0', np.complex_)

    def get_symbol(self):
        return self.symbol

    def get_matrix(self):
        return self.matrix
