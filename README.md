Quantum Circuits
================

Quantum Circuits will be a program to simulate quantum circuits on a classical computer

This program is written to learn a bit more about Python so I'll be heavily refactoring it throughout the project as I learn more.  The circuit model of quantum computation <i>looks</i> a little like a logic gate circuit but with quantum gates.  However, quantum superposition, measurement and the quantum register make things very different!

The project will start off as a command line program but a GUI might be put on top of it using something like Qt later.

Current progress (10th October): All functionality is demonstrated in unit tests only.  Tests show the following:
- Register initialisation
- Common quantum gates can be added to a circuit.  Currently, gates can only be added to a register if the gate acts on n qubits and the register has n qubits
- Stepping forwards through a circuit applies all the gates in the initial step to the register
