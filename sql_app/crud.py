from sqlalchemy.orm import Session

from . import models, schemas

#############################
### Funções a Implementar ###
#############################

def get_filmes(db, limit):
    pass

def get_avaliacoes(db, limit):
    pass

def get_filme_por_id(db, id_filme):
    pass

def get_avaliacoes_por_filme(db, id_filme):
    pass

def create_filme(db, filme):
    pass

def create_avaliacao(db, avaliacao):
    pass

def update_filme(db, id_filme, filme):
    pass

def update_avaliacao(db, id_avaliacao, avaliacao):
    pass

def delete_filme(db, id_filme):
    pass

def delete_avaliacao(db, id_avaliacao):
    pass

########################
### Funções tutorial ###
########################

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item