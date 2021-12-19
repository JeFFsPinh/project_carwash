import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = db.create_engine('sqlite:///db.sqlite3')

Session = sessionmaker(bind=engine)

Base = declarative_base()

def init_app():
    Base.metadata.create_all(engine)
