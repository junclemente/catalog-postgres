#!/usr/bin/python
import sys

flask_path = '/var/www/FlaskApp/'
if flask_path not in sys.path:
    sys.path.insert(0, flask_path)
#sys.path.insert(0, "/var/www/FlaskApp/")

from app import app as application

#application.secret_key = 'secret key'
