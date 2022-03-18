from sqlalchemy import Column, Float, ForeignKey, Integer, String, column
from db import Base, engine
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String(120), unique=True)
    def __repr__(self):
        return f'<User {self.name} {self.email}>'

class Cocktails(Base):
    __tablename__ = 'Cocktails'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    Ingredients = Column(String, unique=True)
    recipe = Column(String)
    commetn = Column(String)
    rating = column(Float(1))
    author = column(String)
    def __repr__(self):
        return f'<Coctails {self.name} {self.Ingredients}>'


#class rating(Base):
 #   __tablename__ = 'Rating'
  #  rating = Column(Integer(5))
    #users_id = Column(Integer, ForeignKey('users.id'))
   # Cocktails_id = Column(Integer, ForeignKey('Cocktails.id'))
    #def __repr__(self):
     #   return f'<Rating {self.rating}>'






if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)