from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/filmes/", response_model=list[schemas.Filmes])
def read_filmes(limit : int = 10, db: Session = Depends(get_db)):
    filmes = crud.get_filmes(db, limit=limit)
    if len(filmes) == 0:
        raise HTTPException(status_code=204, detail="Sem filmes cadastrados")
    return filmes

@app.get("/avaliacaoes/", response_model=list[schemas.Avaliacoes])
def read_avaliacoes(limit : int = 10, db: Session = Depends(get_db)):
    avaliacoes = crud.get_avaliacoes(db, limit=limit)
    if len(avaliacoes) == 0:
        raise HTTPException(status_code=204, detail="Sem avaliações cadastradas")
    return avaliacoes

@app.get("/filmes/{id_filme}", response_model=schemas.Filmes)
def read_filme_por_id(id_filme: int, db: Session = Depends(get_db)):
    filme = crud.get_filme_por_id(db, id_filme=id_filme)
    if filme is None:
        raise HTTPException(status_code=204, detail="Filme não encontrado")
    return filme

@app.get("/avaliacoes/{id_filme}", response_model=list[schemas.Avaliacoes])
def read_avaliacoes_por_filme(id_filme: int, db: Session = Depends(get_db)):
    avaliacoes = crud.get_avaliacoes_por_filme(db, id_filme=id_filme)
    if len(avaliacoes) == 0:
        raise HTTPException(status_code=204, detail="Sem avaliações para o filme especificado")
    return avaliacoes

@app.post("/filmes/", response_model=schemas.Filmes)
def create_filme(filme: schemas.FilmesCreate, db: Session = Depends(get_db)):
    return crud.create_filme(db=db, filme=filme)

@app.post("/avaliacoes/", response_model=schemas.Avaliacoes)
def create_avaliacao(avaliacao: schemas.AvaliacoesCreate, db: Session = Depends(get_db)):
    return crud.create_avaliacao(db=db, avaliacao=avaliacao)

@app.put("/filmes/{id_filme}")
def update_filme(id_filme: int, filme: schemas.FilmesUpdate, db: Session = Depends(get_db)):
    updated_filme = crud.update_filme(db=db, id_filme=id_filme, filme=filme)
    if updated_filme is None:
        raise HTTPException(status_code=204, detail="Filme especificado não existe")
    return updated_filme

@app.put("/avaliacoes/{id_avaliacao}")
def update_avaliacao(id_avaliacao: int, avaliacao: schemas.AvaliacoesUpdate, db: Session = Depends(get_db)):
    updated_avaliacao = crud.update_avaliacao(db=db, id_avaliacao=id_avaliacao, avaliacao=avaliacao)
    if updated_avaliacao is None:
        raise HTTPException(status_code=204, detail="Avaliação especificada não existe")
    return updated_avaliacao

@app.delete("/filmes/{id_filme}")
def delete_filme(id_filme: int, db: Session = Depends(get_db)):
    deleted_filme = crud.delete_filme(db=db, id_filme=id_filme)
    if deleted_filme is None:
        raise HTTPException(status_code=204, detail="Filme especificado não existe")
    return deleted_filme

@app.delete("/avaliacoes/{id_avaliacao}")
def delete_avaliacao(id_avaliacao: int, db: Session = Depends(get_db)):
    deleted_avaliacao = crud.delete_avaliacao(db=db, id_avaliacao=id_avaliacao)
    if deleted_avaliacao is None:
        raise HTTPException(status_code=204, detail="Avaliação especificada não existe")
    return deleted_avaliacao