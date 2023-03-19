from sqlalchemy import Column, Integer, String
from config.database import Base

# Crea una clase que hereda de Base (que es la clase que nos permite interactuar con la base de datos)
class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    year = Column(Integer)
    genre = Column(String)
    