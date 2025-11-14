import random
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

def create_battle_circuit(player_gate, ai_gate):
    """
    Creates the 2-qubit circuit for the game.
    Player is Qubit 0, AI is Qubit 1.
    """
    circuit = QuantumCircuit(2, 1) # 2 qubits, 1 classical bit (for player's)
    
    # 1. Apply each player's chosen gate (starting from |0>)
    if player_gate == 'X':
        circuit.x(0)
    elif player_gate == 'H':
        circuit.h(0)
    elif player_gate == 'I':
        circuit.id(0)  
        
    if ai_gate == 'X':
        circuit.x(1)
    elif ai_gate == 'H':
        circuit.h(1)
    elif ai_gate == 'I':
        circuit.id(1)
        
    circuit.barrier()
    
    # 2. Entangle the two qubits
    # Player (control) entangles with AI (target)
    circuit.cx(0, 1)
    
    circuit.barrier()
    
    # 3. Measure only the player's qubit to decide the winner
    circuit.measure(1, 0)
    
    return circuit

def run_battle(circuit, num_shots=1):
    """Runs the circuit and returns the winner."""
    
    simulator = AerSimulator()
    circuit = transpile(circuit, simulator)
    
    result = simulator.run(circuit, shots=num_shots).result()
    counts = result.get_counts(circuit)
    measurement = list(counts.keys())[0]
    
    print(f"\n--- Circuit Diagram ---")
    print(circuit.draw(output='text'))
    
    if measurement == '1':
        return "Querida"
    else:
        return "Player"
    
    # --- MAIN CODE ---
player_score = 0
ai_score = 0
print("--- Welcome to Quantum Coin Battle! ---")
print("We each have a qubit, starting at |0>.")
print("Each round, we both secretly pick a gate: 'X' (flip) or 'H' (superposition).")
print("We apply our gates, entangle, and measure. If my qubit is 1, I win!")

for i in range(5): # Play 5 rounds
    print(f"\n--- Round {i+1} ---")
    print(f"Score: Player {player_score} - Querida {ai_score}")
    
    # 1. Get Player Move
    player_move = ""
    valid_moves = ['X', 'H', 'I']
    while player_move not in valid_moves:
        player_move = input("Choose your gate (X, H or I): ").upper()
        
    # 2. Get AI Move
    ai_move = random.choice(['X', 'H', 'I'])
    print(f"AI chose: {ai_move}")
    
    # 3. Run the battle
    qc = create_battle_circuit(player_move, ai_move)
    winner = run_battle(qc)
    print(f"\n...Measuring Querida's qubit...")
    print(f"Winner is: {winner}!")
    
    if winner == "Player":
        player_score += 1
    else:
        ai_score += 1

print("\n--- FINAL SCORE ---")
print(f"Player: {player_score}")
print(f"Querida: {ai_score}")
if player_score > ai_score:
    print("You win the hackathon! (and the game)")
else:
    print("The Querida wins! Try to figure out its strategy...")