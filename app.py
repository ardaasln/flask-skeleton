from flask import Flask
from src.errors.error_handlers import handle_custom_error
from src.errors.custom_error import CustomError
from src.http import Http
from flask_pymongo import PyMongo

app = Flask(__name__)
app.wsgi_app = Http(app.wsgi_app)
app.register_error_handler(CustomError, handle_custom_error)
app.config.from_pyfile('./config/config.py', silent=True)

mongo = PyMongo(app)

from src.api.test import bp
app.register_blueprint(bp)

if __name__ == '__main__':
    app.run()

