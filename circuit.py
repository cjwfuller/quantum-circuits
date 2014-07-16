import numpy as np

class Circuit:
    def __init__(self, num_qubits, num_steps):
        self.circuit = [[]]
        init_step = [complex(0,0)] * pow(2, num_qubits)

        # TODO At arbitrary x,y will potentially be a quantum gate