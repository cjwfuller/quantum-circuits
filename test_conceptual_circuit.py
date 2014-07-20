import unittest
import conceptual_circuit as cc
import gate

class TestConceptualCircuit(unittest.TestCase):
    def test_basic_construction(self):
        c = cc.ConceptualCircuit(1, 5)

    def test_circuit_construction_size(self):
        c = cc.ConceptualCircuit(1, 5)
        num_basis = 2
        num_steps = 5

        self.assertEqual(len(c.grid), num_basis)
        for x in c.grid:
            self.assertEqual(len(x), num_steps)

    def test_basic_add_gate(self):
        hadamard = gate.QuantumGate('hadamard')
        row_num = 1
        c = cc.ConceptualCircuit(1, 5)
        c.add_gate(hadamard, row_num)

        self.assertEqual(c.grid[1][0], 'H')

    def test_add_gate_preserves_existing_gates(self):
        hadamard = gate.QuantumGate('hadamard')
        paulix = gate.QuantumGate('paulix')
        row_num = 1
        c = cc.ConceptualCircuit(1, 5)
        c.add_gate(hadamard, row_num)
        c.add_gate(paulix, row_num)

        self.assertEqual(c.grid[1][0], 'H')
        self.assertEqual(c.grid[1][1], 'X')

    def test_add_gate_posn_constraint(self):
        hadamard = gate.QuantumGate('hadamard')
        c = cc.ConceptualCircuit(1, 5)
        self.assertRaises(IndexError, c.add_gate, hadamard, 4)

    def test_add_after_last_step_constraint(self):
        hadamard = gate.QuantumGate('hadamard')
        c = cc.ConceptualCircuit(1, 2)
        row_num = 1
        c.add_gate(hadamard, row_num)
        c.add_gate(hadamard, row_num)
        self.assertRaises(IndexError, c.add_gate, hadamard, row_num)

if __name__ == '__main__':
    unittest.main()