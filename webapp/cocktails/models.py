from webapp.db import db


class Cocktails(db.Model):
    """Создает модель коктейля в БД
    """
    __searchable__ = ['title']
    
    id = db.Column(db.Integer, unique=True, primary_key=True)
    url = db.Column(db.String, unique=True, nullable=False)
    title = db.Column(db.String, unique=True)
    tags = db.Column(db.String)
    recipe = db.Column(db.String)
    ingredient = db.Column(db.String)
    tools = db.Column(db.String)
    image = db.Column(db.String, unique=True)

    def __repr__(self):
        return f"Coctails {self.id} {self.title}"


class Raiting(db.Model):
    """Создает модель рейтинг коктейля
    """

    id = db.Column(db.Integer, unique=True, primary_key=True)
    title = db.Column(db.String, unique=True)
    rating = db.Column(db.Float(1), nullable=True)
    author = db.Column(db.String, unique=True)

    def __repr__(self):
        return f"Raiting {self.id} {self.title}"
