from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Xur_tab(Base):
    __tablename__ = 'Xur_tab'

    id = Column(Integer, primary_key=True)
    Xur_place = Column(Text)