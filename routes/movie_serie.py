from flask import Blueprint, abort, request, jsonify
from flasgger import Swagger, swag_from

from docs.movie_serie import delete_movie_serie_doc, \
    update_movie_serie_doc, create_movie_serie_doc, get_movie_serie_doc
from utils.token import token_required
from controllers.MovieSerieController import MovieSerieController

movie_serie_controller = MovieSerieController()
movie_serie = Blueprint('movie-serie', __name__)

@movie_serie.route('/', methods=['GET'])
@movie_serie.route('/<id>', methods=['GET'])
@swag_from(get_movie_serie_doc)
@token_required
def get(id=None):
    try:
        if id:
            response = movie_serie_controller.get_by_id(id)
        else:
            response = movie_serie_controller.get_all()
        return jsonify(response)
    except:
        abort(404)

@movie_serie.route('/', methods=['POST'])
@swag_from(create_movie_serie_doc)
@token_required
def create():
    try:
        response = movie_serie_controller.create(request.json)
        return jsonify(response)
    except:
        abort(404)

@movie_serie.route('/<id>', methods=['PUT', 'PATCH'])
@swag_from(update_movie_serie_doc)
@token_required
def update(id=None):
    try:
        response = movie_serie_controller.update(id, request.json)
        return jsonify(response)
    except:
        abort(404)

@movie_serie.route('/<id>', methods=['DELETE'])
@swag_from(delete_movie_serie_doc)
@token_required
def delete(id=None):
    try:
        response = movie_serie_controller.delete(id)
        return jsonify(response)
    except:
        abort(404)

