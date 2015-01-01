import numpy as np
import quantum_gate

class PauliYQuantumGate(quantum_gate.QuantumGate):
    def __init__(self):
        super(PauliYQuantumGate, self)
        self.symbol = 'Y'
        self.matrix = np.matrix('0 -1i; 1i 0', np.complex_)
