from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgresql://rueicqqh:hYlexQ-widfhtrmVt2vQMAbGHWRZz339@balarama.db.elephantsql.com:5432/rueicqqh')
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()
