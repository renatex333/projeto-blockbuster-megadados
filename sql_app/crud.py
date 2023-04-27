from sqlalchemy.orm import Session
from sqlalchemy import update

from . import models, schemas

def get_filmes(db: Session, limit: int = 10):
    return db.query(models.Filmes).limit(limit).all()

def get_avaliacoes(db: Session, limit: int = 10):
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
    updated = db.query(models.Filmes).filter(models.Filmes.id_filme == id_filme).update({models.Filmes.nome: filme.nome, models.Filmes.categoria: filme.categoria, models.Filmes.duracao: filme.duracao, models.Filmes.ano: filme.ano})
    if not updated:
        return None
    db.commit()
    return db.query(models.Filmes).filter(models.Filmes.id_filme == id_filme).first()

def update_avaliacao(db: Session, id_avaliacao: int, avaliacao: schemas.AvaliacoesUpdate):
    updated = db.query(models.Avaliacoes).filter(models.Avaliacoes.id_avaliacao == id_avaliacao).update({models.Avaliacoes.nota: avaliacao.nota, models.Avaliacoes.comentario: avaliacao.comentario})
    if not updated:
        return None
    db.commit()
    return db.query(models.Avaliacoes).filter(models.Avaliacoes.id_avaliacao == id_avaliacao).first()

def delete_filme(db: Session, id_filme: int):
    deleted = db.query(models.Filmes).filter(models.Filmes.id_filme == id_filme).delete()
    if not deleted:
        return None
    db.commit()
    return {"status": "success", "message": "Filme deletado"}

def delete_avaliacao(db: Session, id_avaliacao: int):
    deleted = db.query(models.Avaliacoes).filter(models.Avaliacoes.id_avaliacao == id_avaliacao).delete()
    if not deleted:
        return None
    db.commit()
    return {"status": "success", "message": "Avaliação deletada"}