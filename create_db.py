from sqlalchemy import *
from settings import SQLALCHEMY_DATABASE_URI
from model import *

engine = create_engine(SQLALCHEMY_DATABASE_URI)

metadata.create_all(engine)