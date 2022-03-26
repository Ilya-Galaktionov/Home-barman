from webapp.db import db_session
from webapp.models import User

my_user = User.query.first()
db_session.commit()
