import numpy as np
from pprint import pprint

# TODO having a conceptual circuit and quantum circuit is unnecessary - refactor
class QuantumCircuit:

    def __init__(self, num_qubits, num_steps):
        self.step = 0
        self.num_steps = num_steps
        self.num_qubits = num_qubits
        self.num_bases = pow(2, num_qubits)
        self.zeros = np.zeros((self.num_bases, self.num_bases), dtype=np.complex_)

        self.grid = [
            [
                self.zeros for gate in xrange(self.num_qubits)
            ] for n in xrange(self.num_steps)
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
        if self.step == self.num_steps:
            raise IndexError("No free steps to step forwards")
        self.step = self.step + 1

        for idx, basis in enumerate(self.grid[self]):
            print basis

   # TODO
   def measure(self):
        """Perform quantum measurement

        Collapses from quantum state to classical state
        """