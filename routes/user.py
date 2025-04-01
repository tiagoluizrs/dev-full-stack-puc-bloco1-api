from flask import Blueprint, abort, request, jsonify

user = Blueprint('user', __name__)

@user.route('/register', methods=['POST'])
def register():
    try:
        return jsonify({'key': 'value'})
    except:
        abort(404)

@user.route('/login', methods=['POST'])
def login():
    try:
        return jsonify({'key': 'value'})
    except:
        abort(404)
