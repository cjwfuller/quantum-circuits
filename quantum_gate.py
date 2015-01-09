import numpy as np
import gate
import register

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
        x, y = shape[0], shape[1]
        if(x != y):
            raise Exception("Matrix must have dimension n*n")
        # unitary matrices must satisfy U*U = UU* = I
        identity = np.identity(x)
        conjugate_transpose = self.matrix.getH()
        if not (self.matrix * conjugate_transpose).all() == identity.all():
            raise Exception("Matrix must be unitary")

    def get_symbol(self):
        return self.symbol

    def get_matrix(self):
        return self.matrix

    # TODO
    # TODO qubit_nums need to be the same as the gate size
    def resize(self, num_qubits, qubit_nums):
        """Resize a gate to act on a given number of qubits.

        Gates can act on an arbitrary number of qubits but they must be resized
        so they can be applied to the circuit

        Arguments:
        num_qubits -- number of qubits to resize gate to e.g. 3
        qubit_nums -- qubits to act on e.g. [0, 2]
        """
        resized_dimension = pow(2, num_qubits)
        resized = np.zeros((resized_dimension, resized_dimension), dtype=np.complex_)
        filtered_bases = register.Register.filter_bases(num_qubits, qubit_nums)
        new_bases = register.Register.generate_bases(num_qubits)
        for idx, dirac_base in enumerate(filtered_bases):
            vector = register.Register.dirac_to_column_vector(dirac_base)
            # apply fundamental matrix to column vector
            vector = np.squeeze(np.asarray(np.dot(self.get_matrix(), vector)))
            # build the new set of bases vectors
            new_dirac_base = register.Register.column_vector_to_dirac(vector)
            for idy, qubit_num in enumerate(qubit_nums):
                new_bases[idx][qubit_num] = new_dirac_base[idy]
            row = register.Register.dirac_to_column_vector(new_bases[idx])
            # build the resized matrix
            resized[idx] = row
        self.matrix = resized
