import numpy as np
from qiskit.circuit.library import ZZFeatureMap, RealAmplitudes
from qiskit.circuit import QuantumCircuit
from qiskit_machine_learning.neural_networks import EstimatorQNN

class SecQuantumNeuralNetwork:
    """IBM Qiskit-based Quantum Neural Network for classification and prediction tasks"""
    def __init__(self, num_features: int):
        self.num_qubits = num_features
        self._build_qnn_circuit()

    def _build_qnn_circuit(self):
        # 1. Data Embedding Map
        self.feature_map = ZZFeatureMap(feature_dimension=self.num_qubits, reps=1, entanglement='linear')
        
        # 2. Trainable Quantum Layer (Ansatz)
        self.ansatz = RealAmplitudes(num_qubits=self.num_qubits, reps=1, entanglement='linear')
        
        # 3. Merging Circuit Layers
        self.circuit = QuantumCircuit(self.num_qubits)
        self.circuit.append(self.feature_map, range(self.num_qubits))
        self.circuit.append(self.ansatz, range(self.num_qubits))
        
        self.qnn = EstimatorQNN(
            circuit=self.circuit,
            input_params=self.feature_map.parameters,
            weight_params=self.ansatz.parameters
        )
        print(f"[QML] Professional {self.num_qubits}-Qubit QNN Circuit successfully initialized.")

    def forward_pass(self, input_data: np.ndarray, weights: np.ndarray) -> np.ndarray:
        """Executes forward pass prediction on the quantum simulator backend"""
        return self.qnn.forward(input_data, weights)
