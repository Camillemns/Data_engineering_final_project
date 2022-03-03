from typing import Optional
from urllib import request
from fastapi import FastAPI
import time
from fastapi.middleware.cors import CORSMiddleware
from model import prediction_toxicity, load_model,get_model_prediction
from pydantic import BaseModel
from prometheus_client import start_http_server, Counter, Gauge, Summary, Histogram

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

start_http_server(8010)

request_toxicity_counter = Counter('request_toxicity_counter', 'Number of sentence where the toxicity has been predicted.')
in_progress_counter = Gauge('in_progress_counter', 'Number of predictions in progress.')
last_prediction_time = Gauge('last_prediction_time', 'The last time a prediction was done.')

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
    in_progress_counter.inc()
    p = get_model_prediction(items['model'], data.text)
    last_prediction_time.set(time.time())
    in_progress_counter.dec()
    request_toxicity_counter.inc()
    for k, v in p.items():
        p[k] = float(v)
    return {"result": p}
