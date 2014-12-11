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

        num_bases = len(state)
        if(num_bases != pow(2, num_qubits)):
            raise Exception("Invalid number of bases vectors")

        eps = 0.0001
        total = complex(0, 0)
        for s in state:
            total = total + pow(np.abs(s), 2)
        if(not (abs(total - (complex(1, 0))) < eps)):
            raise Exception("Quantum state is invalid")

        self.state = state
        self.num_qubits = num_qubits

    # TODO
    # TODO make me static
    # TODO make me private but still somehow testable
    def generate_bases(self, num_qubits):
        """ Generate bases vectors

        Example: [000, 001, 010, 011, 100, 101, 110, 111] for a 3-qubit system
        """
        bases = []
        base_idx = pow(2, num_qubits) - 1
        while base_idx >= 0:
            base = []
            current_base = base_idx
            for c in xrange(num_qubits):
                base.append(current_base % 2)
                current_base = current_base / 2
            base.reverse()
            bases.append(base)
            base_idx = base_idx - 1
        bases.reverse()
        return bases

    def measure(self):
        """Perform quantum measurement

        Collapses from quantum state to classical state
        qubit_num -- the qubits to measure
        """
        # TODO use a {}?
        # TODO to do this, loop through each bases and do (1/value)^2
        current_state = np.squeeze(np.asarray(self.state))
        probabilities = {}
        for idx, basis in enumerate(current_state):
            probabilities[idx] = pow(basis, 2)
