import math
import numpy as np
import quantum_gate

class HadamardQuantumGate(quantum_gate.QuantumGate):
    def __init__(self):
        super(HadamardQuantumGate, self)
        self.symbol = 'H'
        self.matrix = ((1/math.sqrt(2)+0j) * np.matrix('1 1; 1 -1', np.complex_))
