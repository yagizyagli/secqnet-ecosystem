import os
from setuptools import setup, find_packages

# Read the requirements from requirements.txt safely
with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
    required_packages = f.read().splitlines()

setup(
    name="secqnet",
    version="1.0.0",
    author="SecQNet Developer Team",
    author_email="support@secqnet.io",
    description="An enterprise full-stack library uniting Post-Quantum Cryptography (PQC) and Quantum Machine Learning (QML)",
    long_description="SecQNet bridges the gap between secure network payloads and quantum-accelerated artificial intelligence using IBM Qiskit.",
    long_description_content_type="text/markdown",
    url="https://github.com",
    packages=find_packages(exclude=["tests*", "docs*"]),
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Security :: Cryptography",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.10",
    install_requires=required_packages,
)
