from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

# Python module was created to better organize code
from app import views, models, restful_api, authenticate, forms, catalog_db


# @app.route("/")
# @app.route("/test")
# def test_index():
#     return "Hello World! Test Index! Catalog000"
