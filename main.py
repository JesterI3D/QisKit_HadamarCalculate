""" This program calculates the probability
of flipping a coin using quantum computing
using the Hadamard operator.

Hadamar Formula: H = 1/sqrt(2) [ 1,1 ]
                              [ 1,-1 ]
Operator: |0> -> 1/sqrt(2)[0> + 1/sqrt(2)|1>
"""


from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, Aer

# We use the quantum register to calculate
quantumReg = QuantumRegister(1)

# The result of a quantum register is written in classic
classReg = ClassicalRegister(1)

# Build
superposition_state = QuantumCircuit(quantumReg, classReg)
superposition_state.h(quantumReg)
superposition_state.measure(quantumReg, classReg)

# Execute
# Can use a local backend, as in this case, as well as IBMQ (Cloud Compute om IMB Instanse)
backend = Aer.get_backend('qasm_simulator')
job = execute(superposition_state, backend, shots=1024)
result = job.result()

# Print result

print('quantum probability:\n', result.get_counts(superposition_state))