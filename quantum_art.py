import turtle
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

def create_quantum_art_circuit(num_qubits):
    """Creates an entangled quantum circuit to generate art parameters."""
    circuit = QuantumCircuit(num_qubits)
    
    # Put all qubits in superposition
    circuit.h(range(num_qubits))
    
    for i in range(1, num_qubits):
        circuit.cx(0, i) # Entangle everything back to qubit 0
        
    circuit.measure_all()
    
    print(circuit.draw(output='text'))
    
    return circuit

def get_quantum_instructions(circuit, num_shots=1):
    """Run the circuit and get the measurement bitstring."""
    # Use the 'aer_simulator'
    simulator = AerSimulator()
    circuit = transpile(circuit, simulator)
        
    # We only need one "roll" of the quantum dice
    result = simulator.run(circuit, shots=num_shots).result()
    counts = result.get_counts(circuit)
    
    # Get the first (and only) measurement result
    bitstring = list(counts.keys())[0]
    return bitstring

def draw_art(bitstring):
    """Uses the turtle library to draw art based on the bitstring."""
    t = turtle.Turtle()
    t.speed(1) # Fastest speed
    screen = turtle.Screen()
    screen.bgcolor("#0d001a")
    colors = ["#FF69B4", "#1E90FF", "#00FF7F", "#EE82EE", "#00FFFF", "#FFD700", "#FF00FF", "#7D00FF", "#00BFFF"]
    
    # We'll read the bitstring in 3-bit chunks
    bits_3 = [bitstring[i:i+3] for i in range(0, len(bitstring) - 2, 3)]
    
    for i, move in enumerate(bits_3):
        t.color(colors[i % len(colors)]) # Cycle through colors
        t.width(i // 6 + 1) # Get thicker as we go
        
        if move == '000':
            # "jump" forward without drawing
            t.penup()
            t.forward(15)
            t.pendown()
        elif move == '001':
            t.forward(30)
        elif move == '010':
            t.backward(30)
        elif move == '011':
            t.right(90)
            t.forward(30)
        elif move == '100':
            t.left(90)
            t.forward(30)
        elif move == '101':
            t.right(90)
            t.backward(30)
        elif move == '110':
            t.left(90)
            t.backward(30)
        elif move == '111':
            t.circle(20)
            
    t.screen.exitonclick()
    
# --- MAIN CODE ---
print("Running quantum circuit to generate art...")
NUM_QUBITS = int(input("Enter number of qubits (max 30 for this quantum simulator): ")) # More qubits = longer instruction string!
art_circuit = create_quantum_art_circuit(NUM_QUBITS)
instructions = get_quantum_instructions(art_circuit)

print(f"Quantum Bitstring: {instructions}")
print("Drawing your quantum art...")
draw_art(instructions)