from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model import prediction_toxicity, load_model,get_model_prediction
from pydantic import BaseModel

app = FastAPI()

# NEW
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

items = {}


class PredictionData(BaseModel):
    text: str


@app.on_event("startup")
async def startup_event():
    model = load_model('original')
    items["model"] = model

@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.post("/get_toxicity/")
async def prediction(data: PredictionData):
    p = get_model_prediction(items['model'], data.text)
    return {"message": p}
