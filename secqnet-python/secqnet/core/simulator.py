from qiskit import QuantumCircuit
from qiskit.compiler import transpile
from qiskit_aer import AerSimulator

class QuantumCoreBackend:
    """Manages Qiskit backend connections, circuit transpilation, and execution"""
    def __init__(self, optimize_level: int = 3):
        # Initialize the state-of-the-art Qiskit Aer Simulator
        self.backend = AerSimulator()
        self.optimize_level = optimize_level
        print("[CORE] Quantum Aer Simulator backend successfully loaded.")

    def execute_circuit(self, circuit: QuantumCircuit) -> dict:
        """Transpiles and executes the quantum circuit on the selected backend"""
        # Transpilation optimizes the circuit for the physical hardware/simulator topology
        transpiled_circuit = transpile(circuit, self.backend, optimization_level=self.optimize_level)
        job = self.backend.run(transpiled_circuit, shots=1024)
        result = job.result()
        
        # Returns the measurement counts (e.g., {'00': 512, '11': 512})
        return result.get_counts()
