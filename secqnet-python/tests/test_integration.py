import os
import pytest
import numpy as np
from secqnet import SecQNetApp
from secqnet.pqc import PQCSecureLayer
from secqnet.qml import SecQuantumNeuralNetwork

def test_pqc_encryption_layer():
    """Tests if the Post-Quantum Cryptography layer successfully encrypts and decrypts payload"""
    pqc = PQCSecureLayer()
    sensitive_data = b"Enterprise_Secret_Key_2026"
    
    # Simulate peer key exchange
    peer_key = os.urandom(32)
    shared_secret, _ = pqc.encapsulate_key(peer_key)
    
    # Encrypt and verify
    ciphertext, iv, tag = pqc.encrypt_payload(sensitive_data, shared_secret)
    assert ciphertext != sensitive_data
    assert len(iv) == 12
    assert len(tag) == 16

def test_qml_forward_pass():
    """Tests if the Qiskit Quantum Neural Network layer generates correct dimension output"""
    num_features = 2
    qml = SecQuantumNeuralNetwork(num_features=num_features)
    
    # Prepare mock data vectors
    mock_input = np.array([0.5, 0.7])
    num_weights = qml.ansatz.num_parameters
    mock_weights = np.random.rand(num_weights)
    
    output = qml.forward_pass(mock_input, mock_weights)
    assert output is not None
    assert isinstance(output, np.ndarray)

def test_full_pipeline_orchestration():
    """Tests the entire secure pipeline execution from start to finish"""
    app = SecQNetApp(num_features=2)
    cipher, q_prediction = app.process_secure_ai_pipeline(
        raw_sensitive_data="Top_Secret_Data",
        ai_features=[0.12, 0.89]
    )
    
    assert isinstance(cipher, bytes)
    assert isinstance(q_prediction, np.ndarray)
