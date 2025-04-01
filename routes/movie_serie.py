from flask import Blueprint, abort, request, jsonify

from utils.token import token_required

movie_serie = Blueprint('movie-serie', __name__)

@movie_serie.route('/', methods=['GET'])
@movie_serie.route('/<id>', methods=['GET'])
@token_required
def get(id=None):
    try:
        return jsonify({'key': 'value'})
    except:
        abort(404)

@movie_serie.route('/', methods=['POST'])
@token_required
def create():
    try:
        return jsonify({'key': 'value'})
    except:
        abort(404)

@movie_serie.route('/<id>', methods=['PUT', 'PATCH'])
@token_required
def update(id=None):
    try:
        return jsonify({'key': 'value'})
    except:
        abort(404)

@movie_serie.route('/<id>', methods=['DELETE'])
@token_required
def delete(id=None):
    try:
        return jsonify({'key': 'value'})
    except:
        abort(404)