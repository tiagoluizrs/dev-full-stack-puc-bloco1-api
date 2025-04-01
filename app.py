from flask import Flask
from routes.user import user
from routes.movie_serie import movie_serie

app = Flask(__name__)
app.register_blueprint(user)
app.register_blueprint(movie_serie)