from routes.auth import auth
from routes.movie_serie import movie_serie
from routes.rating import rating

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
import os

# Inicialização do app
app = Flask(__name__)
swagger = Swagger(app)

# Configurações do banco de dados
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, "database.db")
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DATABASE_PATH}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Inicializando a instância do SQLAlchemy
db = SQLAlchemy(app)

# with app.app_context():
#     from models.User import User
#     from models.MovieSerie import MovieSerie
#     from models.Rating import Rating
#     db.create_all()


app.register_blueprint(auth)
app.register_blueprint(movie_serie)
app.register_blueprint(rating)