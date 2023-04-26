from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Get lista filmes
@app.get("/filmes/", response_model=list[schemas.Filmes])
def read_filmes(db: Session = Depends(get_db)):
    filmes = crud.get_filmes(db)
    return filmes

# Get lista avaliacoes
@app.get("/avaliacaoes/", response_model=list[schemas.Avaliacoes])
def read_avaliacoes(db: Session = Depends(get_db)):
    avaliacoes = crud.get_avaliacoes(db)
    return avaliacoes

# Get filme por id
@app.get("/filmes/{id_filme}", response_model=schemas.Filmes)
def read_filme_por_id(id_filme: int, db: Session = Depends(get_db)):
    filme = crud.get_filme_por_id(db, id_filme=id_filme)
    if filme is None:
        raise HTTPException(status_code=404, detail="Filme not found")
    return filme

# Get avaliacoes por filme
@app.get("/avaliacoes/{id_filme}", response_model=list[schemas.Avaliacoes])
def read_avaliacao_por_filme(id_filme: int, db: Session = Depends(get_db)):
    avaliacoes = crud.get_avaliacoes_por_filme(db, id_filme=id_filme)
    if avaliacoes is None:
        raise HTTPException(status_code=404, detail="Avaliações not found")
    return avaliacoes

# Post filme
@app.post("/filmes/", response_model=schemas.Filmes)
def create_filme(filme: schemas.FilmesCreate, db: Session = Depends(get_db)):
    return crud.create_filme(db=db, filme=filme)

# Post avaliacao
@app.post("/avaliacoes/", response_model=schemas.Avaliacoes)
def create_avaliacao(avaliacao: schemas.AvaliacoesCreate, db: Session = Depends(get_db)):
    return crud.create_avaliacao(db=db, avaliacao=avaliacao)

#######################    
### Continuar daqui ###
#######################

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
    for id_avaliacao, avaliacao in list(dicio_avaliacoes.items()):
        if avaliacao["id_filme"] == id_filme:
            del dicio_avaliacoes[id_avaliacao]
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