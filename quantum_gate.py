import numpy as np

import gate
import register as r

class QuantumGate(gate.Gate):
    """
    super(<name of child class>, self) should be called before any methods in
    QuantumGate are called
    """

    def __new__(cls, *args, **kwargs):
        if cls is QuantumGate:
            raise TypeError("quantum gate class may not be instantiated")
        return object.__new__(cls, *args, **kwargs)

    def __init__(self):
        """Determine whether the gate is quantum

        This is done by determining whether the gate has a unitary matrix"""
        shape = np.shape(self.matrix)
        # unitary matrices will always have dimension n*n
        width, height = shape[0], shape[1]
        if width != height:
            raise Exception("Matrix must have dimension n*n")
        # unitary matrices must satisfy U*U = UU* = I
        identity = np.identity(width)
        conjugate_transpose = self.matrix.getH()
        if not (self.matrix * conjugate_transpose).all() == identity.all():
            raise Exception("Matrix must be unitary")

    def get_symbol(self):
        return self.symbol

    def get_matrix(self):
        return self.matrix

    def get_num_qubits(self):
        return self.num_qubits

    def resize(self, num_qubits, qubit_nums):
        """Resize a gate to act on a given number of qubits.

        Gates can act on an arbitrary number of qubits but they must be resized
        so they can be applied to the circuit

        Arguments:
        num_qubits -- number of qubits to resize gate to e.g. 3
        qubit_nums -- qubits to act on e.g. [0, 2]
        """
        if self.get_num_qubits() != len(qubit_nums):
            raise ValueError("Invalid number of qubit numbers given")

        resized_dimension = pow(2, num_qubits)
        resized = np.zeros((resized_dimension, resized_dimension), dtype=np.complex_)
        filtered_bases = r.Register.filter_bases(num_qubits, qubit_nums)
        new_bases = r.Register.generate_bases(num_qubits)
        for idx, dirac_base in enumerate(filtered_bases):
            vector = r.Register.dirac_to_column_vector(dirac_base)
            # apply fundamental matrix to column vector
            vector = np.squeeze(np.asarray(np.dot(self.get_matrix(), vector)))
            # build the new set of bases vectors
            new_dirac_bases = r.Register.column_vector_to_possible_dirac_vectors(vector)
            for idy, qubit_num in enumerate(qubit_nums):
                for new_dirac_base in new_dirac_bases:
                    new_bases[idx][qubit_num] = new_dirac_base[idy]
            row = r.Register.dirac_to_column_vector(new_bases[idx])
            # build the resized matrix
            resized[idx] = row
        self.matrix = resized
