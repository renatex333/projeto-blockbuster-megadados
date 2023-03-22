from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Filme(BaseModel):
    id_filme: int
    nome: str
    categoria: str
    duracao: int
    ano: int

class Avaliacao(BaseModel):
    id_avaliacao: int
    id_filme: int
    nota: int
    comentario: str | None = Field(default=None, title="Comentário da avaliação", max_length=300)


@app.get("/")
async def read_root():
    return {"Hello": "World"}

# Get lista filmes
@app.get("/filmes/")
async def read_filmes():
    return None

# Get lista avaliacoes
@app.get("/avaliacaoes/")
async def read_avaliacoes():
    return None

# Get filme por id
@app.get("/filmes/{id_filme}")
async def read_filme_por_id(id_filme: int):
    return None

# Get avaliacoes por filme
@app.get("/avaliacoes/{id_filme}")
async def read_avaliacao_por_id(id_avaliacao: int):
    return None

# Post filme
@app.post("/filmes/")
async def create_filme(filme: Filme):
    filme_dict = filme.dict()
    return filme_dict

# Post avaliacao
@app.post("/avalicaoes/")
async def create_avaliacao(avaliacao: Avaliacao):
    avaliacao_dict = avaliacao.dict()
    return avaliacao_dict

# Put filme
@app.put("/filmes/{id_filme}")
def update_filme(id_filme: int, filme: Filme):
    filme_dict = filme.dict()
    return filme_dict

# Put avaliacao
@app.put("/avaliacoes/{id_avaliacao}")
def update_avaliacao(id_avaliacao: int, avaliacao: Avaliacao):
    avaliacao_dict = avaliacao.dict()
    return avaliacao_dict

# Delete filme
@app.delete("/filmes/{id_filme}")
def delete_filme(id_filme: int):
    return None

# Delete avaliacao
@app.delete("/avaliacoes/{id_avaliacao}")
def delete_avaliacao(id_avaliacao: int):
    return None