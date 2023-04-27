from sqlalchemy.orm import Session
from sqlalchemy import update

from . import models, schemas

#############################
### Funções a Implementar ###
#############################

def get_filmes(db: Session, limit: int):
    return db.query(models.Filmes).limit(limit).all()

def get_avaliacoes(db: Session, limit: int):
    return db.query(models.Avaliacoes).limit(limit).all()

def get_filme_por_id(db: Session, id_filme: int):
    return db.query(models.Filmes).filter(models.Filmes.id_filme == id_filme).first()

def get_avaliacoes_por_filme(db, id_filme):
    return db.query(models.Avaliacoes).filter(models.Avaliacoes.id_filme == id_filme).all()

def create_filme(db: Session, filme: schemas.FilmesCreate):
    db_filme = models.Filmes(nome=filme.nome, categoria=filme.categoria, duracao=filme.duracao, ano=filme.ano)
    db.add(db_filme)
    db.commit()
    db.refresh(db_filme)
    return db_filme

def create_avaliacao(db: Session, avaliacao: schemas.AvaliacoesCreate):
    db_avaliacao = models.Avaliacoes(id_filme=avaliacao.id_filme, nota=avaliacao.nota, comentario=avaliacao.comentario)
    db.add(db_avaliacao)
    db.commit()
    db.refresh(db_avaliacao)
    return db_avaliacao

def update_filme(db: Session, id_filme: int, filme: schemas.FilmesUpdate):
    db_filme = db.execute("filmes".update().where(models.Filmes.id_filme == id_filme).values(nome=filme.nome, categoria=filme.categoria, duracao=filme.duracao, ano=filme.ano))
    db.commit()
    db.refresh("filmes")
    return db_filme

def update_avaliacao(db: Session, avaliacao: schemas.AvaliacoesUpdate):
    db_avaliacao = db.execute(update("avaliacoes").where(models.Avaliacoes.id_avaliacao == avaliacao.id_avaliacao).values(nota=avaliacao.nota, comentario=avaliacao.comentario))
    db.commit()
    db.refresh("avaliacoes")
    return db_avaliacao

def delete_filme(db: Session, id_filme: int):
    db_filme = db.delete(models.Filmes).where(models.Filmes.id_filme == id_filme)
    db.commit()
    db.refresh("filmes")
    return db_filme

def delete_avaliacao(db: Session, id_avaliacao: int):
    db_avaliacao = db.delete(models.Avaliacoes).where(models.Avaliacoes.id_avaliacao == id_avaliacao)
    db.commit()
    db.refresh("avaliacoes")
    return db_avaliacao