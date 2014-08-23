import unittest
import quantum_circuit as qc
import gate

class TestQuantumCircuit(unittest.TestCase):

    def test_basic_construction(self):
        """Construction should not raise any exceptions"""
        c = qc.QuantumCircuit(1, 5)

    def test_qc_construction_size(self):
        """"Construction should make a quantum circuit correctly

        The number of steps, number of qubits and gate dimensions should all
        be correct"""
        num_qubits = 1
        num_basis = 2
        num_steps = 5

        c = qc.QuantumCircuit(num_qubits, num_steps)

        self.assertEqual(len(c.grid), num_steps)
        for step in c.grid:
            for gate in step:
                self.assertEqual(len(gate), num_basis)

    def test_add_gate(self):
        """Adding a quantum gate, works

        When a quantum gate is added, the correct gate should be added to the
        correct place"""
        num_qubits = 1
        num_steps = 5
        qubit_num = 0
        step = 0

        c = qc.QuantumCircuit(num_qubits, num_steps)
        paulix = gate.QuantumGate('paulix')
        c.add_gate(paulix, qubit_num)

        self.assertEqual(c.grid[step][qubit_num].symbol, paulix.symbol)

    def test_two_gates_same_qubit(self):
        """Adding two quantum gates to the same first qubit, works

        The second gate should be added after the first on the same qubit
        """
        num_qubits = 1
        num_steps = 5
        qubit_num = 0
        paulix_step = 0
        pauliy_step = 1

        c = qc.QuantumCircuit(num_qubits, num_steps)
        paulix = gate.QuantumGate('paulix')
        pauliy = gate.QuantumGate('pauliy')
        c.add_gate(paulix, qubit_num)
        c.add_gate(pauliy, qubit_num)

        self.assertEqual(c.grid[paulix_step][qubit_num].symbol, paulix.symbol)
        self.assertEqual(c.grid[pauliy_step][qubit_num].symbol, pauliy.symbol)

    def test_add_after_last_step_constraint(self):
        """Adding a gate after last position, fails"""
        num_qubits = 1
        num_steps = 2
        qubit_num = 0
        paulix_step = 0
        pauliy_step = 1

        c = qc.QuantumCircuit(num_qubits, num_steps)
        paulix = gate.QuantumGate('paulix')
        pauliy = gate.QuantumGate('pauliy')
        c.add_gate(paulix, qubit_num)

        self.assertRaises(Exception, c.add_gate, paulix, 1)

    def test_add_gate_posn_constraint(self):
        """Adding a gate to invalid position, fails"""
        num_qubits = 1
        num_steps = 2

        c = qc.QuantumCircuit(num_qubits, num_steps)
        paulix = gate.QuantumGate('paulix')

        self.assertRaises(Exception, c.add_gate, paulix, 2)

    def test_add_gate_too_large_constraint(self):
        """Adding a gate too big for circuit, fails

        Adding a Hadamard gate (2-qubits) to a 1-qubit system, fails
        """
        num_qubits = 1
        num_steps = 2

        c = qc.QuantumCircuit(num_qubits, num_steps)
        hadamard = gate.QuantumGate('hadamard')

        self.assertRaises(Exception, c.add_gate, hadamard, 1)

    def test_maintain_step(self):
        """Stepping forwards, maintains the circuit position

        When the circuit is moved forwards, the step should be incremented
        """
        num_qubits = 1
        num_steps = 5

        c = qc.QuantumCircuit(num_qubits, num_steps)

        self.assertEqual(c.step, 0)
        c.step_forwards()
        self.assertEqual(c.step, 1)

if __name__ == '__main__':
    unittest.main()