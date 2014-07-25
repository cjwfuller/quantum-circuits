class Register:
    def __init__(self, num_qubits):
        self.state = [complex(0,0)] * pow(2, num_qubits)