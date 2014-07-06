class Register:
    def __init__(self, num_qubits):
        self.basis = [complex(0,0)] * pow(2, num_qubits)