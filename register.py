import math
import random

import numpy as np

class Register(object):
    def __init__(self, num_qubits, state):
        """Initialise quantum register

        A register can be in a measured state superposition of states e.g.
        if a Hadamard gate is applied to a 1-qubit system then the qubit
        would be in a superposition of being both 0 and 1

        The state of the register must always follow this equation:
        Let a, b and c be complex numbers representing the quantum states of a
        2-qubit system: |a|^2 + |b|^2 + |c|^2 + |d|^2 = 1

        Arguments:
        num_qubits -- number of qubits in register e.g. 3
        state -- column vector representing initial quantum state. Example:
            [
                (0.0, 0.0i) # 0 0
                (0.0, 0.0i) # 0 1
                (1.0, 0.0i) # 1 0
                (0.0, 0.0i) # 1 1
            ]
        shows a 'collapsed quantum state' because 1 0 is the only state set to 1
        """
        num_bases = len(state)
        if num_bases != pow(2, num_qubits):
            raise Exception("Invalid number of bases vectors")

        eps = 0.0001
        total = complex(0, 0)
        for val in state:
            total = total + pow(np.abs(val), 2)
        if(not (abs(total - (complex(1, 0))) < eps)):
            raise Exception("Quantum state is invalid")

        self.state = state
        self.num_qubits = num_qubits

    @staticmethod
    def generate_bases(num_qubits):
        """Generate bases vectors

        Arguments:
        num_qubits -- number of qubits in register e.g. 3

        Example: [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0,
        1], [1, 1, 0], [1, 1, 1]] for a 3-qubit system
        """
        bases = []
        num_vectors = pow(2, num_qubits)
        for idx in range(num_vectors):
            base = []
            current_base = idx
            for _ in range(num_qubits):
                base.append(current_base % 2)
                current_base = current_base / 2
            base.reverse()
            bases.append(base)
        return bases

    @staticmethod
    def filter_bases(num_qubits, qubit_nums):
        """Filter bases

        Arguments:
        num_qubits -- number of qubits in register e.g. 3
        qubit_nums -- the qubits to filter e.g. 0 and 2

        Example:
            - Generate bases: [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1,
            0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
            - Filter to qubits 0 and 2: [[0, 0], [0, 1], [0, 0], [0, 1], [1,
              0], [1, 1], [1, 0], [1, 1]]
        """
        bases = Register.generate_bases(num_qubits)
        for idx in xrange(len(bases)):
            bases_before_filter = bases[idx]
            bases[idx] = []
            for qubit_position in qubit_nums:
                bases[idx].append(bases_before_filter[qubit_position])
        return bases

    @staticmethod
    def dirac_to_column_vector(dirac):
        """Convert Dirac vector from to column vector form

        Arguments:
        dirac -- dirac vector to convert e.g. [0, 0]

        Example:
            [0, 0] (|00> in Dirac notation) returns [0, 0, 0, 1]
        """
        binary_str = ''
        for val in dirac:
            binary_str = binary_str + str(val)
        column_vector_len = pow(2, len(dirac))
        one_position = column_vector_len - int(binary_str, 2) - 1
        vector = [0] * column_vector_len
        vector[one_position] = 1
        return vector

    @staticmethod
    def column_vector_to_possible_dirac_vectors(column):
        """Convert column vector to all possible Dirac vectors

        Arguments:
        column -- column vector to convert e.g. [0, 0, 0, 1]

        Examples:
             [0, 0, 0, 1] returns [0, 0]
             (or |00> in Dirac notation)

             [0, 0, 1/sqrt(2), 1/sqrt(2)] returns [0, 0] or [0, 1]
             (or |00> or |01> in Dirac notation)
        """
        possibilities = []
        len_column = len(column)
        num_qubits = int(math.sqrt(len_column))
        bases = Register.generate_bases(num_qubits)
        for idx, number in enumerate(column):
            if number != 0:
                possibilities.append(bases[len_column - idx - 1])
        return possibilities

    def __get_collapsed_qubit__(self, probabilities):
        """Get a random qubit to collapse to based on quantum state

        Arguments:
        probabilities -- probabilities of each state to be the collapse state e.g. [0.5, 0.5]
        """
        r = random.uniform(0, 1)
        s = 0
        for qubit, prob in enumerate(probabilities):
            s += probabilities[prob]
            if s >= r:
                return qubit
        return probabilities[-1]

    # TODO
    def measure(self):
        """Perform quantum measurement

        Collapses from quantum state to classical state
        """
        # TODO use a {}?
        # TODO to do this, loop through each bases and do (1/value)^2
        current_state = np.squeeze(np.asarray(self.state))
        probabilities = {}
        for idx, basis in enumerate(current_state):
            probabilities[idx] = pow(basis, 2)
        collapsed_qubit = self.__get_collapsed_qubit__(probabilities)
        for idx, basis in enumerate(current_state):
            current_state[idx] = 0
        current_state[collapsed_qubit] = 1
        self.state = np.asmatrix(current_state)
