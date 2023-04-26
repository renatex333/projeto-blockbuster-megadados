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
def read_filmes(limit : int = 100, db: Session = Depends(get_db)):
    filmes = crud.get_filmes(db, limit=limit)
    return filmes

# Get lista avaliacoes
@app.get("/avaliacaoes/", response_model=list[schemas.Avaliacoes])
def read_avaliacoes(limit : int = 100, db: Session = Depends(get_db)):
    avaliacoes = crud.get_avaliacoes(db, limit=limit)
    return avaliacoes

# Get filme por id
@app.get("/filmes/{id_filme}", response_model=schemas.Filmes)
def read_filme_por_id(id_filme: int, db: Session = Depends(get_db)):
    filme = crud.get_filme_por_id(db, id_filme=id_filme)
    if filme is None:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    return filme

# Get avaliacoes por filme
@app.get("/avaliacoes/{id_filme}", response_model=list[schemas.Avaliacoes])
def read_avaliacoes_por_filme(id_filme: int, db: Session = Depends(get_db)):
    avaliacoes = crud.get_avaliacoes_por_filme(db, id_filme=id_filme)
    if avaliacoes is None:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")
    return avaliacoes

# Post filme
@app.post("/filmes/", response_model=schemas.Filmes)
def create_filme(filme: schemas.FilmesCreate, db: Session = Depends(get_db)):
    return crud.create_filme(db=db, filme=filme)

# Post avaliacao
@app.post("/avaliacoes/", response_model=schemas.Avaliacoes)
def create_avaliacao(avaliacao: schemas.AvaliacoesCreate, db: Session = Depends(get_db)):
    return crud.create_avaliacao(db=db, avaliacao=avaliacao)

# Put filme
@app.put("/filmes/{id_filme}", response_model=schemas.Filmes)
def update_filme(id_filme: int, filme: schemas.FilmesCreate, db: Session = Depends(get_db)):
    updated_filme = crud.update_filme(db=db, id_filme=id_filme, filme=filme)
    if updated_filme is None:
        raise HTTPException(status_code=204, detail="Filme especificado não existe")
    return updated_filme

# Put avaliacao
@app.put("/avaliacoes/{id_avaliacao}", response_model=schemas.Avaliacoes)
def update_avaliacao(id_avaliacao: int, avaliacao: schemas.AvaliacoesCreate, db: Session = Depends(get_db)):
    updated_avaliacao = crud.update_avaliacao(db=db, id_avaliacao=id_avaliacao, avaliacao=avaliacao)
    if updated_avaliacao is None:
        raise HTTPException(status_code=204, detail="Avaliação especificada não existe")
    return updated_avaliacao

# Delete filme
@app.delete("/filmes/{id_filme}", response_model=schemas.Filmes)
def delete_filme(id_filme: int, db: Session = Depends(get_db)):
    deleted_filme = crud.delete_filme(db=db, id_filme=id_filme)
    if deleted_filme is None:
        raise HTTPException(status_code=204, detail="Filme especificado não existe")
    return deleted_filme

# Delete avaliacao
@app.delete("/avaliacoes/{id_avaliacao}", response_model=schemas.Avaliacoes)
def delete_avaliacao(id_avaliacao: int, db: Session = Depends(get_db)):
    deleted_avaliacao = crud.delete_avaliacao(db=db, id_avaliacao=id_avaliacao)
    if deleted_avaliacao is None:
        raise HTTPException(status_code=204, detail="Avaliação especificada não existe")
    return deleted_avaliacao