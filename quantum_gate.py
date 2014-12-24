import numpy as np
import gate
import register

class QuantumGate(gate.Gate):
    def get_symbol(self):
        return self.symbol

    def get_matrix(self):
        return self.matrix

    def __is_unitary(self):
        """Determine whether the gate is unitary"""
        shape = np.shape(self.matrix)
        # unitary matrices will always have dimension n*n
        x, y = shape[0], shape[1]
        if(x != y):
            return False
        # unitary matrices must satisfy U*U = UU* = I
        identity = np.identity(x)
        conjugate_transpose = self.matrix.getH()
        return (self.matrix * conjugate_transpose).all() == identity.all()

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
        filtered_bases = register.Register.filter_bases(num_qubits, qubit_nums)
        for dirac_base in filtered_bases:
            vector = register.Register.dirac_to_column_vector(dirac_base)
            print vector
            #print vector * self.get_matrix
