from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel, Field

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
    return {"Hello": "World"}

# Get lista filmes
@app.get("/filmes/")
async def read_filmes():
    return dicio_filmes

# Get lista avaliacoes
@app.get("/avaliacaoes/")
async def read_avaliacoes():
    return dicio_avaliacoes

# Get filme por id
@app.get("/filmes/{id_filme}")
async def read_filme_por_id(id_filme: int):
    return dicio_filmes[id_filme] if id_filme in dicio_filmes else None

# Get avaliacoes por filme
@app.get("/avaliacoes/{id_filme}")
async def read_avaliacao_por_id(id_avaliacao: int):
    return dicio_avaliacoes[id_avaliacao] if id_avaliacao in dicio_avaliacoes else None

# Post filme
@app.post("/filmes/")
async def create_filme(filme: Filme):
    filme_dict = filme.dict()
    dicio_filmes[id_filme_generico] = filme_dict
    id_filme_generico += 1
    return filme_dict

# Post avaliacao
@app.post("/avalicaoes/")
async def create_avaliacao(avaliacao: Avaliacao):
    avaliacao_dict = avaliacao.dict()
    dicio_avaliacoes[id_filme_generico] = avaliacao_dict
    id_avaliacao_generico += 1
    return avaliacao_dict

# Put filme
@app.put("/filmes/{id_filme}")
def update_filme(id_filme: int, filme: Filme):
    filme_dict = filme.dict()
    dicio_filmes[id_filme] = filme_dict
    return filme_dict

# Put avaliacao
@app.put("/avaliacoes/{id_avaliacao}")
def update_avaliacao(id_avaliacao: int, avaliacao: Avaliacao):
    avaliacao_dict = avaliacao.dict()
    dicio_avaliacoes[id_avaliacao] = avaliacao_dict
    return avaliacao_dict

# Delete filme
@app.delete("/filmes/{id_filme}")
def delete_filme(id_filme: int):
    del dicio_filmes[id_filme]
    return None

# Delete avaliacao
@app.delete("/avaliacoes/{id_avaliacao}")
def delete_avaliacao(id_avaliacao: int):
    del dicio_avaliacoes[id_avaliacao]
    return None