Quantum Circuits
================

Quantum Circuits will be a program to simulate quantum circuits on a classical computer

This program is written to learn a bit more about Python so I'll be heavily refactoring it throughout the project as I learn more.  The circuit model of quantum computation <i>looks</i> a little like a logic gate circuit but with quantum gates.  However, quantum superposition, measurement and the quantum register make things very different!

The project will start off as a command line program but a GUI might be put on top of it using something like Qt later.

Current progress (17th May 2015): All functionality is demonstrated in unit tests only.  It can be shown that a Hadamard gate can be added to a single qubit circuit and when the circuit runs, the Hadamard gate is applied to the qubit.  When a measurement is performed, the qubit will collapse to either a 1 or 0 with probabilities of 0.5.  Current work is ensuring that more qubits and gates can be simulated and that gates can be re-sized.
