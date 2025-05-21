# from services.request import Request
#
# http = Request()
#
# http.search('89815000')

from fastapi import FastAPI

from services.request import Request

app = FastAPI()

@app.get("/")
def test():
    return {"data": "teste"}

@app.get("/search_cep={cep}")
def search_cep(cep):

    requestApi = Request()
    return {"data": cep}
