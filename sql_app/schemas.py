from pydantic import BaseModel, Field


class AvaliacoesBase(BaseModel):
    nota: int
    comentario: str | None = Field(default=None, title="Comentário da avaliação", max_length=200)


class AvaliacoesCreate(AvaliacoesBase):
    pass

class AvaliacoesUpdate(AvaliacoesBase):
    id_avaliacao: int


class Avaliacoes(AvaliacoesBase):
    id_avaliacao: int
    id_filme: int

    class Config:
        orm_mode = True


class FilmesBase(BaseModel):
    nome: str
    categoria: str
    duracao: int
    ano: int


class FilmesCreate(FilmesBase):
    pass

class FilmesUpdate(FilmesBase):
    pass

class Filmes(FilmesBase):
    id_filme: int

    class Config:
        orm_mode = True