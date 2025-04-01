from flask import Blueprint, abort, request, jsonify
from flasgger import Swagger, swag_from

from docs.rating import rating_doc
from utils.token import token_required
from controllers.RatingController import RatingController

rating_controller = RatingController()
rating = Blueprint('rating', __name__)

@rating.route('/<id>', methods=['POST', 'PUT', 'PATCH'])
@swag_from(rating_doc)
@token_required
def new_or_update_rating(id=None):
    try:
        response = rating_controller.rating(id, request.json)
        return jsonify(response)
    except:
        abort(404)