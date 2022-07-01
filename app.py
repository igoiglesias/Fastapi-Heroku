from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def index():
    return {"message": "oi"}

@app.get('/fulano/{nome}')
async def fulano(nome: str):
    return {"message": f"oi {nome}"}