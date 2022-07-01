from fastapi import FastAPI
from model.custom_model import Teste

app = FastAPI()

@app.get('/')
async def index():
    return {"message": "oi"}

@app.get('/fulano/{nome}')
async def fulano(nome: str):
    return {"message": f"oi {nome}"}

@app.post('/fulano')
async def fulano(nome: Teste):
    return {"message": f"oi {nome}"}