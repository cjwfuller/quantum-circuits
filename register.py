import math
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

    # TODO make me private but still somehow testable
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
        base_idx = 0
        for idx in range(num_vectors):
            base = []
            current_base = idx
            for idy in range(num_qubits):
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
        for base_num, base in enumerate(bases):
            bases_before_filter = bases[base_num]
            bases[base_num] = []
            for qubit_position in qubit_nums:
                bases[base_num].append(bases_before_filter[qubit_position])
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
        for d in dirac:
            binary_str = binary_str + str(d)
        num_qubits = pow(len(dirac), 2)
        one_position = num_qubits - int(binary_str, 2) - 1
        vector = [0] * num_qubits
        vector[one_position] = 1
        return vector

    @staticmethod
    def column_vector_to_dirac(column):
        """Convert vector from to Dirac form to column vector

        Arguments:
        column -- column vector to convert e.g. [0, 0, 0, 1]

        Example:
             [0, 0, 0, 1] returns [0, 0] (|00> in Dirac notation)
        """
        len_column = len(column)
        num_qubits = int(math.sqrt(len_column))
        bases = Register.generate_bases(num_qubits)
        try:
            one_position = tuple(column).index(1)
        except:
            raise Exception("Supplied column vector contained no '1' value")
        return bases[len_column - one_position - 1]

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
