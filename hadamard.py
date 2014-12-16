import math
import numpy as np
import gate

class HadamardQuantumGate(gate.QuantumGate):
    def __init__(self):
        self.symbol = 'H'
        self.matrix = ((1/math.sqrt(2)+0j) * np.matrix('1 1; 1 -1', np.complex_))

    def get_symbol(self):
        return self.symbol

    def get_matrix(self):
        return self.matrix
