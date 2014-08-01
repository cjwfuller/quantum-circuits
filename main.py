import register
import conceptual_circuit
import quantum_circuit
import sys

num_qubits = input("How many qubits should this circuit have? ")
num_steps = input("How many steps should this circuit have? ")

register = register.Register(num_qubits)
conceptual_circuit = conceptual_circuit.ConceptualCircuit(num_qubits, num_steps)
quantum_circuit = quantum_circuit.QuantumCircuit(num_qubits, num_steps)

print "\nRegister is initialised.  Choose an option:"
print "    1 - add a gate"
print "    2 - print circuit"
print "    3 - step forwards"
print "    4 - run circuit"

# TODO
while True:
    option = input("Choice: ")
    if(oprion == 1):
        print "Uninplemented"
    if(option == 2):
        conceptual_circuit.display()
    elif(option == 3):
        conceptual_circuit.step_forwards()
    else:
        print "Unrecognised option.  Re-enter choice: "
