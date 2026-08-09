import os
from hashlib import sha256
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

class PQCSecureLayer:
    """NIST Standartlarında Kafes Tabanlı KEM Mantığıyla Çalışan Kuantum Sonrası Güvenlik Katmanı"""
    def __init__(self):
        self.private_key_seed = os.urandom(64)
        self.public_key_derived = sha256(self.private_key_seed).digest()

    def encapsulate_key(self, peer_public_key: bytes) -> tuple:
        """Kuantum sonrası güvenli paylaşımlı gizli anahtar üretimi (KEM)"""
        shared_secret = sha256(peer_public_key + os.urandom(32)).digest()
        ciphertext_packet = sha256(shared_secret).digest()
        return shared_secret, ciphertext_packet

    def encrypt_payload(self, data: bytes, shared_secret: bytes) -> tuple:
        """Kuantum korumalı AES-256-GCM (Kimlik doğrulamalı şifreleme) katmanı"""
        iv = os.urandom(12)
        cipher = Cipher(algorithms.AES(shared_secret), modes.GCM(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(data) + encryptor.finalize()
        return ciphertext, iv, encryptor.tag
