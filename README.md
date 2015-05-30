Quantum Circuits
================

Simulate quantum circuits on a classical computer.

All functionality is demonstrated in unit tests only.  It can be shown that a Hadamard gate can be added to a single qubit circuit and when the circuit runs, the Hadamard gate is applied to the qubit.  When a measurement is performed, the qubit will collapse to either a 1 or 0 with probabilities of 0.5.

Proposed extensions to this project (Pull Requests welcome!):
- Tests to ensure that more qubits and gates can be simulated
- Tests to ensure that gates can be re-sized (e.g. adding and applying a Hadamard gate (1-qubit gate) to a 2-qubit system)
- A User Interface (command-line or graphical)
- Preloaded quantum circuits

The circuit model of quantum computation <i>looks</i> a little like a logic gate circuit but with quantum gates.  However, quantum superposition, measurement and the quantum register make things very different.
