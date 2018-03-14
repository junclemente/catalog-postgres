from app import app

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# engine = create_engine('sqlite:///catalogProject.db')
# engine = create_engine('postgresql://student:student@localhost/catalog000')
engine = create_engine(app.config['DATABASE_URI'])
# engine = create_engine('postgresql://catalogowner:cat000@localhost/catalog')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
