import unittest
import math
import numpy as np
import quantum_circuit as qc
import gates.paulix as paulix
import gates.pauliy as pauliy
import gates.hadamard as hadamard
import register

class TestQuantumCircuit(unittest.TestCase):
    def test_basic_construction(self):
        """Construction should not raise any exceptions"""
        state = np.array([1/math.sqrt(2), 1/math.sqrt(2)], dtype=np.complex_)
        r = register.Register(1, state)
        c = qc.QuantumCircuit(r, 5)

    def test_qc_construction_size(self):
        """"Construction should make a quantum circuit correctly

        The number of steps and gate dimensions should all be correct"""
        num_steps = 5

        state = np.array([1/math.sqrt(2), 1/math.sqrt(2)], dtype=np.complex_)
        r = register.Register(1, state)
        c = qc.QuantumCircuit(r, num_steps)

        self.assertEqual(len(c.grid), num_steps)
        for step in c.grid:
            for gate in step:
                self.assertIsNone(gate)

    def test_add_gate(self):
        """Adding a quantum gate, works

        When a quantum gate is added, the correct gate should be added to the
        correct place"""
        num_steps = 5
        qubit_num = 0
        step = 0

        state = np.array([1/math.sqrt(2), 1/math.sqrt(2)], dtype=np.complex_)
        r = register.Register(1, state)
        c = qc.QuantumCircuit(r, num_steps)
        gate = paulix.PauliXQuantumGate()
        c.add_gate(gate, qubit_num)

        self.assertEqual(c.grid[step][qubit_num].symbol, gate.get_symbol())

    def test_two_gates_same_qubit(self):
        """Adding two quantum gates to the same first qubit, works

        The second gate should be added after the first on the same qubit
        """
        num_steps = 5
        qubit_num = 0
        paulix_step = 0
        pauliy_step = 1

        state = np.array([1/math.sqrt(2), 1/math.sqrt(2)], dtype=np.complex_)
        r = register.Register(1, state)
        c = qc.QuantumCircuit(r, num_steps)
        paulix_gate = paulix.PauliXQuantumGate()
        pauliy_gate = pauliy.PauliYQuantumGate()
        c.add_gate(paulix_gate, qubit_num)
        c.add_gate(pauliy_gate, qubit_num)

        self.assertEqual(c.grid[paulix_step][qubit_num].symbol,
                paulix_gate.get_symbol())
        self.assertEqual(c.grid[pauliy_step][qubit_num].symbol,
                pauliy_gate.get_symbol())

    def test_add_after_last_step_constraint(self):
        """Adding a gate after last position, fails"""
        num_steps = 1
        qubit_num = 0

        state = np.array([1/math.sqrt(2), 1/math.sqrt(2)], dtype=np.complex_)
        r = register.Register(1, state)
        c = qc.QuantumCircuit(r, num_steps)
        gate = paulix.PauliXQuantumGate()
        c.add_gate(gate, qubit_num)

        self.assertRaises(Exception, c.add_gate, gate, qubit_num)

    def test_add_gate_posn_constraint(self):
        """Adding a gate to invalid position, fails"""
        num_steps = 2

        state = np.array([1/math.sqrt(2), 1/math.sqrt(2)], dtype=np.complex_)
        r = register.Register(1, state)
        c = qc.QuantumCircuit(r, num_steps)
        gate = paulix.PauliXQuantumGate()

        self.assertRaises(Exception, c.add_gate, gate, 2)

    def test_add_gate_too_large_constraint(self):
        """Adding a gate too big for circuit, fails

        Adding a Hadamard gate (2-qubits) to a 1-qubit system, fails
        """
        num_steps = 1

        state = np.array([1/math.sqrt(2), 1/math.sqrt(2)], dtype=np.complex_)
        r = register.Register(1, state)
        c = qc.QuantumCircuit(r, num_steps)
        gate = hadamard.HadamardQuantumGate()
        c.add_gate(gate, 0)

        self.assertRaises(Exception, c.add_gate, gate, 1)

    def test_maintain_step(self):
        """Stepping forwards, maintains the circuit position

        When the circuit is moved forwards, the step should be incremented
        """
        num_steps = 5

        state = np.array([1/math.sqrt(2), 1/math.sqrt(2)], dtype=np.complex_)
        r = register.Register(1, state)
        c = qc.QuantumCircuit(r, num_steps)

        self.assertEqual(c.step, 0)
        c.step_forwards()
        self.assertEqual(c.step, 1)

    def test_basic_step_forwards(self):
        """Stepping forwards, applies a gate"""
        num_steps = 3

        s = np.array([1, 0], dtype=np.complex_)
        r = register.Register(1, s)
        c = qc.QuantumCircuit(r, num_steps)
        gate = hadamard.HadamardQuantumGate()
        c.add_gate(gate, 0)
        c.step_forwards()

        final_state = np.squeeze(np.asarray(c.register.state))
        self.assertEqual(final_state[0], 1/math.sqrt(2))
        self.assertEqual(final_state[1], 1/math.sqrt(2))

    # TODO
    def test_basic_measure(self):
        """Measuring, collapses quantum state"""
        num_steps = 3

        s = np.array([1, 0], dtype=np.complex_)
        r = register.Register(1, s)
        c = qc.QuantumCircuit(r, num_steps)
        gate = hadamard.HadamardQuantumGate()
        c.add_gate(gate, 0)
        c.step_forwards()
        c.register.measure()

if __name__ == '__main__':
    unittest.main()