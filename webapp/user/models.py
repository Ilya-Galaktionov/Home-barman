from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from ..db import Base
from sqlalchemy import Column, Integer, String


class User(Base, UserMixin):
    """Создает модель пользователя в БД
    """
    __tablename__ = 'Users'

    id = Column(Integer, unique=True, primary_key=True)
    username = Column(String(50), index=True, unique=True)
    password = Column(String(128))
    role = Column(String(10), index=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def is_admin(self):
        return self.role == 'admin'

    def __repr__(self):
        return f"User {self.id} {self.username}"
