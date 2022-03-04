from typing import Optional
from urllib import request
from fastapi import FastAPI
import time
from fastapi.middleware.cors import CORSMiddleware
from model import prediction_toxicity, load_model,get_model_prediction
from pydantic import BaseModel
from prometheus_client import start_http_server, Counter, Gauge, Summary, Enum

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
prediction_latency_seconds = Summary('prediction_latency_seconds', 'Summary of the time a prediction takes.')
state = Enum('state', 'State of the app.', states=['starting', 'running', 'predicting', 'stopped'])
class PredictionData(BaseModel):
    text: str


@app.on_event("startup")
async def startup_event():
    state.state('starting')
    model = load_model('original')
    items["model"] = model
    state.state('running')


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.post("/get_toxicity/")
async def prediction(data: PredictionData):
    state.state('predicting')
    start = time.time()
    in_progress_counter.inc()
    p = get_model_prediction(items['model'], data.text)
    in_progress_counter.dec()
    request_toxicity_counter.inc()
    prediction_latency_seconds.observe(time.time() - start)
    for k, v in p.items():
        p[k] = float(v)
    return {"result": p}

@app.on_event("shutdown")
def shutdown_event():
    state.state('stopped')
