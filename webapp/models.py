from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Float, Integer, String
from .db import Base, engine

db = SQLAlchemy()


class Cocktails(Base):
    """Создает модель коктейля в БД
    """
    __tablename__ = 'Cocktails'

    id = Column(Integer, unique=True, primary_key=True)
    url = Column(String, unique=True, nullable=False)
    title = Column(String, unique=True)
    tags = Column(String)
    recipe = Column(String)
    ingredient = Column(String)
    tools = Column(String)
    image = Column(String, unique=True)
    
    def __repr__(self):
        return f"Coctails {self.id} {self.title}"


class Raiting(Base):
    """Создает модель рейтинг коктейля
    """
    __tablename__ = 'Raiting'

    id = Column(Integer, unique=True, primary_key=True)
    title = Column(String, unique=True)
    rating = Column(Float(1), nullable=True)
    author = Column(String, unique=True)

    def __repr__(self):
        return f"Raiting {self.id} {self.title}"


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
