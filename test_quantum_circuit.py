import unittest
import circuit
import gate

class TestCircuit(unittest.TestCase):
    def test_basic_construction(self):
        c = circuit.Circuit(1, 5)

    def test_circuit_construction_size(self):
        c = circuit.Circuit(1, 5)

        num_basis = 2
        num_steps = 5

        self.assertEqual(len(c.grid), num_basis)
        for x in c.grid:
            self.assertEqual(len(x), num_steps)

    def test_add_gate(self):
        c = circuit.Circuit(1, 5)
        basis = 0
        hadamard = gate.QuantumGate('hadamard')
        c.add_gate(hadamard, 1)

    def test_step_forwards(self):
        c = quantum_circuit.QuantumCircuit(1, 5)
        self.assertEqual(c.step, 0)
        c.step_forwards()
        self.assertEqual(c.step, 1)

    # TODO
    def test_add_after_last_step_constraint(self):
        self.fail()

    # TODO
    def test_add_gate_posn_constraint(self):
        self.fail()

    # TODO
    def test_add_gate_too_large_constraint(self):
        self.fail()

    # TODO
    def test_add_gate_too_small_constraint(self):
        self.fail()

if __name__ == '__main__':
    unittest.main()