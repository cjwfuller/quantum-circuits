import register
import gate
import conceptual_circuit
import quantum_circuit
import sys

num_qubits = input("How many qubits should this circuit have? ")
num_steps = input("How many steps should this circuit have? ")

register = register.Register(num_qubits)
conceptual_circuit = conceptual_circuit.ConceptualCircuit(num_qubits, num_steps)
quantum_circuit = quantum_circuit.QuantumCircuit(num_qubits, num_steps)

def print_options():
    print "Choose an option:"
    print "    1 - add a gate"
    print "    2 - print circuit"
    print "    3 - step forwards"
    print "    4 - run circuit"
    print "    5 - exit"

print "\nRegister is initialised."
print_options()

# TODO add gate fails second time
# TODO invalid input handling
# TODO split into functions
# TODO use quantum circuit and conceptual circuit
while True:
    option = input("Choice: ")
    if(option == 1):
        print "\nAvailable gates:"
        print "    paulix"
        print "    pauliy"
        print "    pauliz"
        print "    cnot"
        print "    swap"
        print "    toffoli"
        print "    hadamard"
        print "Enter gate to add: "
        gate_name = raw_input("Gate choice: ")
        row_num = input("First row number: ")
        gate = gate.QuantumGate(gate_name)
        conceptual_circuit.add_gate(gate, row_num)
        print "Gate added"
        print_options()
    elif(option == 2):
        conceptual_circuit.display()
        print_options()
    elif(option == 3):
        conceptual_circuit.step_forwards()
        print "Stepped forwards"
        print_options()
    elif(option == 5):
        print "Bye!"
        break;
    else:
        print "Unrecognised option."
        print_options()
