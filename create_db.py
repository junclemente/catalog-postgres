#!/usr/bin/env python
"""
This file is used to initialize a database for this project.
"""
from app import app

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from app.models import User, Category, Item, Base


engine = create_engine('sqlite:///catalogProject.db')
# Bind the engine to the metadata of the Base class so that decleratives can
# be accessed through a DBSession instance
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
# DBSession() instance establishes all converstations with the DB and
# represents a staging zone for all ojbects loaded into the DB session object.
# Any change made against the objects in the session won't be persisted into
# the DB until it is commited by calling: session.commit(). Changes can be
# reverted to the last commit by calling: session.rollback()
session = DBSession()


# Create 'master' user.
user1 = User(username="master")
user1.hash_password("12345")
session.add(user1)
session.commit()
print "Created user: 'master', password: '12345'"


# Create initial category
category1 = Category(name="Snowboard",
                     user_id="1",
                     description="Snowboarding is a recreational activity...")
session.add(category1)
session.commit()

category2 = Category(name="Skiing",
                     user_id="1",
                     description="Skiing is a recreational activity...")
session.add(category2)
session.commit()


# Create initial item
item1 = Item(name="Merc",
             maker="Flow",
             model_year="2017",
             category_id="1",
             user_id="1",
             description="Beginner to Intermediate snowboard.")
session.add(item1)
session.commit()

item2 = Item(name="Aero Coiler Boa",
             maker="Flow",
             model_year="2018",
             category_id="1",
             user_id="1",
             description="Snowboard Boots, 2017")
session.add(item2)
session.commit()

item3 = Item(name="Five Hybrid Snowboard Bindings",
             maker="Flow",
             model_year="2018",
             category_id="1",
             user_id="1",
             description="Snowboard Bindings")
session.add(item3)
session.commit()
print "Created category and items"

