from sqlalchemy import *

md = MetaData()

Xur_tab = Table('Xur_tab', md,
    Column('id', Integer, primary_key=True),
    Column('Xur_place', Text, nullable=False)
)