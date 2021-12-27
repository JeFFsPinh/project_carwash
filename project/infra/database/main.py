import os
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = db.create_engine('sqlite:///db.sqlite3', connect_args={'check_same_thread': False})

Session = sessionmaker(bind=engine)

Base = declarative_base()

def init_app():
    if not os.path.isfile('db.sqlite3'):
        Base.metadata.create_all(engine)
