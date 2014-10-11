import numpy as np
from pprint import pprint
import register

class QuantumCircuit:

    def __init__(self, register, num_steps):
        self.step = 0
        self.num_steps = num_steps
        self.register = register

        self.grid = [
            [
                None for gate in xrange(register.num_qubits)
            ] for n in xrange(num_steps)
        ]

    # TODO
    def __resize_gate(self, gate):
        """Resize a gate to be the same size as the number of basis vectors.

        gates can act on an arbitrary number of qubits but they must be
        resized so they can be applied to the circuit
        """

    def add_gate(self, gate, qubit_num):
        """Add a gate to the circuit.

        Arguments:
        gate -- the quantum gate to add to the circuit
        qubit_num -- the first qubit the gate should act on
        """
        step = 0
        while True:
            if step == self.num_steps:
                raise IndexError("No room for gate")
            if(self.grid[step][qubit_num] is None):
                self.grid[step][qubit_num] = gate
                break
            step = step + 1

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