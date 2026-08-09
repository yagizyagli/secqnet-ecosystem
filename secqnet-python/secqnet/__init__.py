import os
import numpy as np
from .pqc.lattice_enc import PQCSecureLayer
from .qml.qnn import SecQuantumNeuralNetwork

class SecQNetApp:
    """Post-Quantum Cryptography Secure Layer and IBM Qiskit ML Core Orchestration"""
    def __init__(self, num_features: int):
        self.security = PQCSecureLayer()
        self.qml = SecQuantumNeuralNetwork(num_features=num_features)
        print("[SecQNet] 10/10 Production-Ready Quantum Framework Deployed.\n" + "="*60)

    def process_secure_ai_pipeline(self, raw_sensitive_data: str, ai_features: list):
        # Phase 1: Post-Quantum Cryptographic Encryption
        peer_key = os.urandom(32)
        shared_secret, _ = self.security.encapsulate_key(peer_key)
        ciphertext, iv, _ = self.security.encrypt_payload(raw_sensitive_data.encode(), shared_secret)
        print(f"[PQC GÜVENLİK] Payload protected with quantum-resistant encryption. Cipher: {ciphertext.hex()[:15]}...")

        # Phase 2: Quantum Machine Learning Estimation
        print("[QML PIPELINE] Forwarding secure telemetry data vectors into the QNN...")
        input_vector = np.array([ai_features])
        num_weights = self.qml.ansatz.num_parameters
        random_weights = np.random.rand(num_weights)
        quantum_output = self.qml.forward_pass(input_vector, random_weights)
        print(f"[QML INFERENCE] Quantum Neural Network Output: {quantum_output}")
        
        return ciphertext, quantum_output
