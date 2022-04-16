from flask_sqlalchemy import SQLAlchemy
from flask_msearch import Search

db = SQLAlchemy()
search = Search(db=db)
