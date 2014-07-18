import numpy as np

class Circuit:
    def __init__(self, num_qubits, num_steps):
        size = pow(2, num_qubits)
        zeros = np.zeros((size, size), dtype=np.complex_)

        self.grid = [
            [
                [
                    zeros for gate in xrange(num_qubits)
                ] for step in xrange(num_steps)
            ] for n in xrange(size)
        ]