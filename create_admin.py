from getpass import getpass
import sys
import logging

from webapp.user.models import User
from webapp import create_app, db


app = create_app()

with app.app_context():
    username = input('Введите имя пользователя:')

    if User.query.filter(User.username == username).count():
        logging.info('Пользователь с таким именем уже существует!')
        sys.exit(0)

    password1 = getpass('Введите пароль:')
    password2 = getpass('Повторите пароль:')

    if not password1 == password2:
        logging.info('Пароль не совпадает')
        sys.exit(0)

    new_user = User(username=username, role='admin')
    new_user.set_password(password1)

    db.session.add(new_user)
    db.session.commit()
    logging.info(f'Создан пользователь с id={new_user.id}')
