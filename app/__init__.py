from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

# Python module was created to better organize code
from app import views, models, restful_api, authenticate, forms, catalog_db

#import views

# @app.route("/")
# @app.route("/test")
# def test_index():
#     return "<h1>Hello World!</h1> Test Index! Catalog on Lightsail Amazon AAWS."

#if __name__ == "__main__":
#    app.run()
