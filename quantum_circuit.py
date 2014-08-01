import numpy as np

class QuantumCircuit:
    """Quantum Circuit.

    Low-level 2D array of complex-valued quantum gates and associated
    operations
    """
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

    # TODO
    def __resize_gate(self, gate):
        """Resize a gate to be the same size as the number of basis vectors.

        gates can act on an arbitrary number of qubits but they must be
        resized so they can be applied to the circuit
        """

    # TODO
    def add_gate(self, gate, control_qubits, target_qubit):
        """Add a gate to the circuit.

        Arguments:
        gate -- the quantum gate to add to the circuit
        target_qubit --
        selected_qubits -- the qubits that the gate should act on
        """

    # TODO
    def step_forwards(self):
        """Apply gates in next step to register"""

   # TODO
   def measure(self):
        """Perform quantum measurement

        Collapses from quantum state to classical state
        """