import cirq
q = cirq.NamedQubit("q0")
circuit = cirq.Circuit(cirq.H(q), cirq.measure(q))
result = cirq.Simulator().run(circuit)
print(result) 