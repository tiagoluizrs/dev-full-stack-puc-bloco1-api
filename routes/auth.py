from flask import Blueprint, abort, request, jsonify
from flasgger import Swagger, swag_from

from controllers.AuthenticationController import AuthenticationController
from docs.auth import register_doc, login_doc

auth_controller = AuthenticationController()
auth = Blueprint('/', __name__)

@auth.route('/register', methods=['POST'])
@swag_from(register_doc)
def register():
    try:
        response = auth_controller.register(request.json)
        if response:
            return jsonify(response.serialize()), 201
        else:
            return jsonify({'error': 'User already exists'}), 400
    except:
        abort(404)

@auth.route('/login', methods=['POST'])
@swag_from(login_doc)
def login():
    try:
        response = auth_controller.login(request.json)
        if response:
            return jsonify(
                {
                    'user': response.user.serialize(),
                    'token': response.token.generate_token()
                }
            ), 200
        else:
            return jsonify({'error': 'User not found'}), 404
    except:
        abort(404)
