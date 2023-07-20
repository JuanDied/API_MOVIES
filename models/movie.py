from config.database import Base
from sqlalchemy import Column, Integer,Float, String, DateTime, Boolean, ForeignKey

class Movie(Base):

    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    director = Column(String(100), nullable=False)
    year = Column(Integer, nullable=False)
    overview = Column(String(100), nullable=False)
    rating = Column(Float, nullable=False)
    genre = Column(String(100), nullable=False)




