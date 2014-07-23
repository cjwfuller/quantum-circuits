import gate

class ConceptualCircuit:
    """Conceptual Quantum Circuit.

    Users interact with the 'conceptual' quantum circuit as opposed to the
    more low-level, 2D array of complex-valued matrices.

    The conceptual circuit stores the positions of quantum gates.  Gates are
    represented by alphabetic characters.
    """
    def __init__(self, num_qubits, num_steps):
        size = pow(2, num_qubits)

        self.step = 0
        self.num_steps = num_steps
        self.grid = [
            [
                '-' for gate in xrange(num_steps)
            ] for step in xrange(size)
        ]

    def add_gate(self, gate, row_num):
        """Add a gate to the conceptual circuit.

        The gate is added to the leftmost free position in the desired row."""
        step = 0
        while True:
            if step == self.num_steps:
                raise IndexError("No free steps to add gate to requested row")
            if self.grid[row_num][step] == '-':
                self.grid[row_num][step] = gate.symbol
                break
            step = step + 1

    def display(self):
        """Convenience method to print the circuit to stdout."""
        for row in self.grid:

    def step_forwards(self):
        """Step forwards through the circuit.

        Stepping forwards increases the step number which is used to inform
        the user how far through the circuit they are."""
        if self.step == self.num_steps:
            raise IndexError("No free steps to step forwards")
        self.step = self.step + 1