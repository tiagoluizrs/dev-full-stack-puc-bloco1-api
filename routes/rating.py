import logging

from flask import Blueprint, abort, request, jsonify
from flasgger import Swagger, swag_from

from docs.rating import rating_doc
from utils.token import token_required
from controllers.RatingController import RatingController

rating_controller = RatingController()
rating = Blueprint('rating', __name__)

logging.basicConfig(level=logging.DEBUG)

@rating.route('<id>', methods=['POST'])
@swag_from(rating_doc)
@token_required
def new_or_update_rating(id=None):
    try:
        response = rating_controller.new_rating(id, request.json)
        return jsonify(response)
    except Exception as e:
        logging.error(f"[rating | new_or_update_rating] >> Error in POST or PUT or PATCH request: {e}")
        abort(404)