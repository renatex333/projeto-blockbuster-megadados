from sqlalchemy import Column, ForeignKey, Integer, String, SmallInteger
from sqlalchemy.orm import relationship

from .database import Base


class Filmes(Base):
    __tablename__ = "filmes"

    id_filme = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), index=True)
    categoria = Column(String(80))
    duracao = Column(SmallInteger)
    ano = Column(SmallInteger)

    avaliacoes = relationship("Avaliacoes", back_populates="filme")


class Avaliacoes(Base):
    __tablename__ = "avaliacoes"

    id_avaliacao = Column(Integer, primary_key=True, index=True)
    id_filme = Column(Integer, ForeignKey("filmes.id_filme"))
    nota = Column(SmallInteger)
    comentario = Column(String(200), nullable=True)

    filme = relationship("Filmes", back_populates="avaliacoes")