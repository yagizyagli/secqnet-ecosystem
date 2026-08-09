import axios from 'axios';

export interface QuantumAIResponse {
    ciphertext: string;
    quantumPrediction: number[];
}

export class SecQNetClient {
    private backendUrl: string;

    constructor(backendUrl: string = 'http://localhost:8000') {
        this.backendUrl = backendUrl;
        console.log('[SecQNet-JS] Secure Quantum AI Client successfully initialized.');
    }

    /**
     * Encrypts data via PQC and requests prediction from the Quantum AI model backend
     */
    async processSecurePipeline(sensitiveData: string, aiFeatures: number[]): Promise<QuantumAIResponse> {
        try {
            const response = await axios.post(`${`${this.backendUrl}/api/process`}`, {
                raw_data: sensitiveData,
                features: aiFeatures
            });
            return response.data;
        } catch (error) {
            console.error('[SecQNet-JS] Critical error in quantum pipeline execution:', error);
            throw error;
        }
    }
}
