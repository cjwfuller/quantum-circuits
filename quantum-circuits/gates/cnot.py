import numpy as np
import quantum_gate

class CNOTQuantumGate(quantum_gate.QuantumGate):
    def __init__(self):
        super(CNOTQuantumGate, self)
        self.symbol = 'C'
        self.num_qubits = 2
        self.matrix = np.matrix("""
            1 0 0 0;
            0 1 0 0;
            0 0 0 1;
            0 0 1 0""", np.complex_)
