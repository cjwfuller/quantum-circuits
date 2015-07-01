import numpy as np
import quantum_gate

class PauliXQuantumGate(quantum_gate.QuantumGate):
    def __init__(self):
        super(PauliXQuantumGate, self)
        self.symbol = 'X'
        self.num_qubits = 1
        self.matrix = np.matrix('0 1; 1 0', np.complex_)
