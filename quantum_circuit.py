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
                None for gate in range(register.num_qubits)
            ] for n in range(num_steps)
        ]

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

    def step_forwards(self):
        """Apply gates in next step to register"""
        if self.step == self.num_steps:
            raise IndexError("No free steps to step forwards")
        for gate in self.grid[self.step]:
            if(gate is not None):
               self.register.state = np.dot(self.register.state, gate.matrix)
        self.step = self.step + 1