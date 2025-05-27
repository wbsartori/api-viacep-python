import json
import requests
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

class Item(BaseModel):
    cep: str
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/cep")
def search_cep(item: Item):
    response = requests.get(f'https://viacep.com.br/ws/{int(item.cep)}/json')
    dataApi = response.json()
    data = {}
    data = {
        'status' : response.status_code,
        'message': f"Consultado com sucesso para o CEP: {int(item.cep)}",
        'type': 'success',
        'data': dataApi,
    }
    if 'erro' in dataApi:
        data['message'] = f"Erro ao consultar o CEP: {int(item.cep)}"
        data['type'] = 'error'
        data['data'] = {}
    return data
