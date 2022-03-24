from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Float, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash
from webapp.db import Base, engine

db = SQLAlchemy()


class User(Base, UserMixin):
    __tablename__ = 'Users'

    id = Column(Integer, unique=True, primary_key=True)
    username = Column(String(50), index=True, unique=True)
    password = Column(String(128))
    role = Column(String(10), index=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"User {self.id} {self.username}"


class Cocktails(Base):
    __tablename__ = 'Cocktails'

    id = Column(Integer, unique=True, primary_key=True)
    url = Column(String, unique=True, nullable=False)
    title = Column(String, unique=True)
    tags = Column(String)
    recipe = Column(String)
    ingredient = Column(String)
    tools = Column(String)
    image = Column(String, unique=True)
    commetn = Column(String)
    rating = Column(Float(1), nullable=True)
    author = Column(String, nullable=True)

    def __repr__(self):
        return f"Coctails {self.id} {self.title}"


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)

# class rating(Base):
#     __tablename__ = 'Rating'
#     rating = Column(Integer(5))
#     users_id = Column(Integer, ForeignKey('users.id'))
#     Cocktails_id = Column(Integer, ForeignKey('Cocktails.id'))

#     def __repr__(self):
#         return f'<Rating {self.rating}>'
