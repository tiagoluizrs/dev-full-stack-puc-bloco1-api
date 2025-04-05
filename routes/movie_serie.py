import logging

from flask import Blueprint, abort, request, jsonify
from flasgger import swag_from

from docs.movie_serie import delete_movie_serie_doc, update_movie_serie_doc, create_movie_serie_doc, get_movie_serie_doc
from utils.token import token_required
from controllers.MovieSerieController import MovieSerieController

movie_serie_controller = MovieSerieController()
movie_serie = Blueprint('movie-serie', __name__)

logging.basicConfig(level=logging.DEBUG)

@movie_serie.route('', methods=['GET'])
@movie_serie.route('<id>', methods=['GET'])
@swag_from(get_movie_serie_doc)
@token_required
def get(id=None):
    try:
        if id:
            response = movie_serie_controller.get_by_id(id)
        else:
            page = request.args.get('page', default=1, type=int)
            limit = request.args.get('limit', default=10, type=int)
            type = request.args.get('type', default=None, type=int)
            response = movie_serie_controller.get_all(page=page, limit=limit, type=type)
        return jsonify(response)
    except Exception as e:
        logging.error(f"[movie_serie | get] >> Error in GET request: {e}")
        abort(404)

@movie_serie.route('', methods=['POST'])
@swag_from(create_movie_serie_doc)
@token_required
def create():
    try:
        response = movie_serie_controller.create(request.json)
        return jsonify(response), 201
    except Exception as e:
        logging.error(f"[movie_serie | create] >> Error in POST request: {e}")
        abort(404)