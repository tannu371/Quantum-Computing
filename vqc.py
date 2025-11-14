import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from qiskit_aer import AerSimulator
from qiskit_machine_learning.algorithms.classifiers import VQC
from qiskit_machine_learning.components.feature_maps import ZZFeatureMap
from qiskit_machine_learning.components.ansatze import RealAmplitudes

print("--- Quantum Classifier ---")

# --- 1. Load & Prepare Classical Data ---
print("Loading classical data...")
# Load the breast cancer dataset
X, y = load_breast_cancer(return_X_y=True)

# For a hackathon, we simplify:
# - Use only 2 features (e.g., "mean radius" and "mean texture")
# - This is so our quantum circuit only needs 2 qubits.
X = X[:, :2]

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Scale the data (very important for QML)
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# --- 2. Set up Quantum Components ---
print("Setting up quantum components...")

# Set up the Quantum "backend"
# We'll use the 'statevector_simulator'
q_instance = QuantumInstance(Aer.get_backend('statevector_simulator'), seed_simulator=42, seed_transpiler=42)

# Define the Feature Map (How we "encode" classical data)
# 2 features = 2 qubits
feature_map = ZZFeatureMap(feature_dimension=2, reps=2, entanglement='linear')

# Define the Ansatz (The "trainable" part of the circuit)
# 'reps=3' means we have 3 layers of trainable gates
ansatz = RealAmplitudes(num_qubits=2, reps=3)

# Define the Classical Optimizer (How we "tune" the circuit)
optimizer = COBYLA(maxiter=100) # 100 iterations

# --- 3. Build the VQC ---
print("Building the VQC model...")
# VQC combines all the parts
vqc = VQC(feature_map=feature_map,
          ansatz=ansatz,
          optimizer=optimizer,
          quantum_instance=q_instance)


# --- 4. Train the Model ---
print("Training the quantum model... (This may take a minute)")
vqc.fit(X_train, y_train)


# --- 5. Score the Model ---
print("Testing the model...")
test_accuracy = vqc.score(X_test, y_test)

print(f"\n--- Hackathon Result ---")
print(f"Test Accuracy: {test_accuracy * 100:.2f}%")