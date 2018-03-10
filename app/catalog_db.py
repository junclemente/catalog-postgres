from app import app

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# engine = create_engine('sqlite:///catalogProject.db')
# engine = create_engine('postgresql://student:student@localhost/catalog000')
engine = create_engine(app.config['DATABASE_URI'])
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
