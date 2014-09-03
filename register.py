import math
import numpy as np

class Register:

    def __init__(self, num_qubits, state):
        """Initialise quantum register

        state - column vector representing initial quantum state. Example:
            [
                (0.0, 0.0i) # 0 0
                (0.0, 0.0i) # 0 1
                (1.0, 0.0i) # 1 0
                (0.0, 0.0i) # 1 1
            ]
        shows a "collapsed quantum state" because 1 0 is the only state set to 1

        A register can be in a measured state superposition of states e.g.
        if a Hadamard gate is applied to a 1-qubit system then the qubit
        would be in a superposition of being both 0 and 1

        The state of the register must always follow this equation:
        Let a, b and c be complex numbers representing the quantum states of a
        2-qubit system: |a|^2 + |b|^2 + |c|^2 + |d|^2 = 1
        """

        eps = 0.0001
        total = complex(0, 0)
        for s in state:
            total = total + pow(np.abs(s), 2)
        if(not (abs(total - (complex(1, 0))) < eps)):
            raise Exception("Quantum state is invalid")

        self.state = state
        self.num_qubits = num_qubits
