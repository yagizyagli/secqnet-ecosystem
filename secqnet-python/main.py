import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from secqnet import SecQNetApp

app = FastAPI(title="SecQNet Quantum Core Engine")
quantum_system = SecQNetApp(num_features=2)

class PipelineRequest(BaseModel):
    raw_data: str
    features: list[float]

@app.post("/api/process")
async def process_pipeline(request: PipelineRequest):
    cipher, q_prediction = quantum_system.process_secure_ai_pipeline(
        raw_sensitive_data=request.raw_data,
        ai_features=request.features
    )
    return {
        "ciphertext": cipher.hex(),
        "quantumPrediction": q_prediction.tolist()
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
