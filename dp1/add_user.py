from webapp.db import db_session
from webapp.models import User

first_user = User(name='Иван Петров', email='ivan@example.com')
db_session.add(first_user)
db_session.commit()
