
# bibliotecas ------------------------------------------ #
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib, os
# ------------------------------------------------------ #


# caminhos --------------------------------------------- #
MODEL_PATH = "model.pkl"
VECTORIZER_PATH = "vectorizer.pkl"
# ------------------------------------------------------ #


# verificação do processamento do modelo --------------- #
if not os.path.exists(MODEL_PATH) or not os.path.exists(VECTORIZER_PATH):
    raise RuntimeError("❌ Modelo não encontrado. Execute train.py primeiro!")

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

app = FastAPI(title="LogGuardian AI API", version="2.0")

class LogRequest(BaseModel):
    log_line: str

class AnomalyResponse(BaseModel):
    is_anomaly: bool
    score: float
# ------------------------------------------------------ #

# ativação da predição --------------------------------- #
@app.post("/predict", response_model=AnomalyResponse)
async def predict(req: LogRequest):
    try:
        X = vectorizer.transform([req.log_line])
        pred = model.predict(X)[0]
        score = model.decision_function(X)[0]
        return {"is_anomaly": pred == -1, "score": float(score)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro: {e}")


# status (ok) ------------------------------------------ #
@app.get("/health")
async def health():
    return {"status": "ok", "model_loaded": True}
# ------------------------------------------------------ #