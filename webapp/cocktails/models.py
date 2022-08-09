from webapp.db import db


class Cocktails(db.Model):
    """Создает модель коктейля в БД
    """

    id = db.Column(db.Integer, unique=True, primary_key=True)
    title = db.Column(db.String, unique=True)
    image = db.Column(db.String, unique=True)
    cocktail_tag = db.relationship('Tags', backref='cocktails', lazy='joined')

    def __repr__(self):
        return f"Coctails {self.id} {self.title}"


class Tags(db.Model):
    """Создает модель тегов коктейля
    """

    id = db.Column(db.Integer, unique=True, primary_key=True)
    tags = db.Column(db.String)
    cocktail_id = db.Column(
        db.Integer,
        db.ForeignKey('cocktails.id', ondelete='CASCADE'),
        index=True
    )

    def __repr__(self):
        return f"Tags {self.id}"


class Recipe(db.Model):
    """Создает модель рецепта коктейля
    """

    id = db.Column(db.Integer, unique=True, primary_key=True)
    recipe = db.Column(db.Text)
    cocktail_id = db.Column(
        db.Integer,
        db.ForeignKey('cocktails.id', ondelete='CASCADE'),
        index=True
    )

    def __repr__(self):
        return f"Recipe {self.id} {self.cocktail_id}"


class Ingredients(db.Model):
    """Создает модель ингредиентов коктейля
    """

    id = db.Column(db.Integer, unique=True, primary_key=True)
    ingredient = db.Column(db.Text)
    amount = db.Column(db.Integer, nullable=True)
    unit = db.Column(db.String, nullable=True)
    cocktail_id = db.Column(
        db.Integer,
        db.ForeignKey('cocktails.id', ondelete='CASCADE'),
        index=True
    )

    def __repr__(self):
        return f"Ingredients {self.id} {self.cocktail_id}"


class Tools(db.Model):
    """Создает модель необходимой посуды для коктейля
    """

    id = db.Column(db.Integer, unique=True, primary_key=True)
    tool = db.Column(db.String)
    amount = db.Column(db.Integer, nullable=True)
    unit = db.Column(db.String, nullable=True)
    cocktail_id = db.Column(
        db.Integer,
        db.ForeignKey('cocktails.id', ondelete='CASCADE'),
        index=True
    )

    def __repr__(self):
        return f"Tools {self.id} {self.cocktail_id}"
