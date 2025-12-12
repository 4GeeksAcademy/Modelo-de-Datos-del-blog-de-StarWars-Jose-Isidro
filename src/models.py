from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(nullable=False)
    apellido: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    fecha_de_subscripcion: Mapped[int] = mapped_column(nullable=False)


class Personaje(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(nullable=False)
    genero: Mapped[str] = mapped_column(nullable=True)
    altura: Mapped[float] = mapped_column(nullable=False)
    color_de_ojos:  Mapped[str] = mapped_column(nullable=True)


class Planeta(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(nullable=False)
    clima: Mapped[str] = mapped_column(nullable=False)
    diametro: Mapped[int] = mapped_column(nullable=False)
    terreno: Mapped[str] = mapped_column(nullable=False)


class Favorito(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped['User'] = relationship()

class Personaje_favorito(Favorito):
    personaje_id: Mapped['Personaje'] = relationship()


class Planeta_favorito(Favorito):
    planeta_id: Mapped['Planeta'] = relationship()
