import requests
from fastapi import FastAPI
from services.request import Request

app = FastAPI()

@app.get("/{cep}")
def search_cep(cep: str):
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json')

    if response.status_code != 200:
        return {"error": f"Erro ao consultar o CEP: {response.status_code}"}

    return response.json()