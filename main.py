from typing import Union, Annotated

from fastapi import FastAPI, Response, status, Header
from pydantic import BaseModel, Field

from fastapi.responses import JSONResponse

app = FastAPI()

dicio_filmes = {}
dicio_avaliacoes = {}

id_filme_generico = 0
id_avaliacao_generico = 0


class Filme(BaseModel):
    nome: str
    categoria: str
    duracao: int
    ano: int

class Avaliacao(BaseModel):
    id_filme: int
    nota: int
    comentario: str | None = Field(default=None, title="Comentário da avaliação", max_length=300)


@app.get("/")
async def read_root():
    return {"BlockBuster": "http://127.0.0.1:8000/docs"}

# Get lista filmes
@app.get("/filmes/")
async def read_filmes(response: Response):
    global dicio_filmes
    headers = {"X-Filmes-Count": f"{len(dicio_filmes)}"}
    response.status_code = status.HTTP_200_OK
    return JSONResponse(content=dicio_filmes, headers=headers)

# Get lista avaliacoes
@app.get("/avaliacaoes/")
async def read_avaliacoes(response: Response):
    global dicio_avaliacoes
    headers = {"X-Avaliacoes-Count": f"{len(dicio_avaliacoes)}"}
    response.status_code = status.HTTP_200_OK
    return JSONResponse(content=dicio_avaliacoes, headers=headers)

# Get filme por id
@app.get("/filmes/{id_filme}")
async def read_filme_por_id(id_filme: int, response: Response):
    global dicio_filmes
    if id_filme not in dicio_filmes.keys():
        response.status_code = status.HTTP_404_NOT_FOUND
        return None
    response.status_code = status.HTTP_200_OK
    return dicio_filmes[id_filme]

# Get avaliacoes por filme
@app.get("/avaliacoes/{id_avaliacao}")
async def read_avaliacao_por_id(id_avaliacao: int, response: Response):
    global dicio_avaliacoes
    if id_avaliacao not in dicio_avaliacoes.keys():
        response.status_code = status.HTTP_404_NOT_FOUND
        return None
    response.status_code = status.HTTP_200_OK
    return dicio_avaliacoes[id_avaliacao]

# Post filme
@app.post("/filmes/")
async def create_filme(filme: Filme, response: Response):
    global dicio_filmes, id_filme_generico
    filme_dict = filme.dict()
    dicio_filmes[id_filme_generico] = filme_dict
    headers = {"X-Link-Filme": f"http://127.0.0.1:8000/filmes/{id_filme_generico}"}
    id_filme_generico += 1
    response.status_code = status.HTTP_201_CREATED
    return JSONResponse(content=filme_dict, headers=headers)

# Post avaliacao
@app.post("/avaliacoes/")
async def create_avaliacao(avaliacao: Avaliacao, response: Response):
    global dicio_avaliacoes, id_avaliacao_generico
    avaliacao_dict = avaliacao.dict()
    dicio_avaliacoes[id_avaliacao_generico] = avaliacao_dict
    headers = {"X-Link-Avaliacao": f"http://127.0.0.1:8000/filmes/{id_avaliacao_generico}"}
    id_avaliacao_generico += 1
    response.status_code = status.HTTP_201_CREATED
    return JSONResponse(content=avaliacao_dict, headers=headers)

# Put filme
@app.put("/filmes/{id_filme}")
def update_filme(id_filme: int, filme: Filme, response: Response):
    global dicio_filmes
    if id_filme not in dicio_filmes.keys():
        response.status_code = status.HTTP_404_NOT_FOUND
        return None
    filme_dict = filme.dict()
    dicio_filmes[id_filme] = filme_dict
    response.status_code = status.HTTP_201_CREATED
    return filme_dict

# Put avaliacao
@app.put("/avaliacoes/{id_avaliacao}")
def update_avaliacao(id_avaliacao: int, avaliacao: Avaliacao, response: Response):
    global dicio_avaliacoes
    if id_avaliacao not in dicio_avaliacoes.keys():
        response.status_code = status.HTTP_404_NOT_FOUND
        return None
    avaliacao_dict = avaliacao.dict()
    dicio_avaliacoes[id_avaliacao] = avaliacao_dict
    response.status_code = status.HTTP_201_CREATED
    return avaliacao_dict

# Delete filme
@app.delete("/filmes/{id_filme}")
def delete_filme(id_filme: int, response: Response):
    global dicio_filmes
    if id_filme not in dicio_filmes.keys():
        response.status_code = status.HTTP_404_NOT_FOUND
        return None
    del dicio_filmes[id_filme]
    response.status_code = status.HTTP_204_NO_CONTENT
    return None

# Delete avaliacao
@app.delete("/avaliacoes/{id_avaliacao}")
def delete_avaliacao(id_avaliacao: int, response: Response):
    global dicio_avaliacoes
    if id_avaliacao not in dicio_avaliacoes.keys():
        response.status_code = status.HTTP_404_NOT_FOUND
        return None
    del dicio_avaliacoes[id_avaliacao]
    response.status_code = status.HTTP_204_NO_CONTENT
    return None