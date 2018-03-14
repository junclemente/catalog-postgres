from app import app

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base


DATABASE_URI = app.config['DATABASE_URI']
engine = create_engine(DATABASE_URI)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
